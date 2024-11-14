import os
import secrets
import bcrypt
import jwt
import datetime
from flask import Flask, request, jsonify
from keras._tf_keras.keras.models import load_model
import numpy as np
import pydicom
import cv2
import json
from functools import wraps
from flask_cors import CORS  
from scripts.preprocessing_utils import preprocess_image
from scripts.database import init_db, add_user, get_user 

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', secrets.token_hex(32)) 

model_path = 'models/new_trained_multioutput_model.keras'
model = load_model(model_path)
print(f"Model loaded from {model_path}")

with open('models/label_mapping.json', 'r') as f:
    label_mapping_rev = {int(v): k for k, v in json.load(f).items()}

with open('models/disease_label_mapping.json', 'r') as f:
    disease_label_mapping_rev = {int(v): k for k, v in json.load(f).items()}

with open('models/sequence_tag_mapping.json', 'r') as f:
    sequence_tag_mapping_rev = {int(v): k for k, v in json.load(f).items()}

init_db()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 403

        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 403

        return f(*args, **kwargs)
    return decorated

# API endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # Add the user to the database
    if add_user(email, password):
        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'error': 'User already exists'}), 409

# API endpoint for login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    stored_password_hash = get_user(email)

    if stored_password_hash and bcrypt.checkpw(password.encode(), stored_password_hash.encode()):
        token = jwt.encode({
            'user': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

def preprocess_dicom_image(dicom_path):
    dcm = pydicom.dcmread(dicom_path)
    extracted_sequence = dcm.get('SequenceName', 'UNKNOWN')
    
    # Extract pixel data and normalize
    image = dcm.pixel_array
    image = cv2.resize(image, (128, 128))  # Resize to model input size
    image = image / np.max(image)  # Normalize pixel values to [0, 1]
    image = np.expand_dims(image, axis=(0, -1))  # Add batch and channel dimensions
    
    return image, extracted_sequence

def predict_and_format(dicom_path):
    """Predict on a single DICOM image and return hierarchical output along with patient metadata."""
    try:
        dicom_image = pydicom.dcmread(dicom_path)
        pixel_array = dicom_image.pixel_array
        
        patient_name = getattr(dicom_image, "PatientName", "Unknown")
        patient_sex = getattr(dicom_image, "PatientSex", "Unknown")
        patient_age = getattr(dicom_image, "PatientAge", "Unknown")

        preprocessed_image = preprocess_image(pixel_array, is_dicom=True).reshape(1, 128, 128, 1)
        
        predictions = model.predict(preprocessed_image)
        
        pred_sequence_probs = predictions[0]
        pred_seq_tag_probs = predictions[1]
        pred_disease_probs = predictions[2]
        
        pred_sequence = np.argmax(pred_sequence_probs, axis=1)[0]
        pred_seq_tag = np.argmax(pred_seq_tag_probs, axis=1)[0]
        pred_disease = np.argmax(pred_disease_probs, axis=1)[0]
        
        sequence_name = label_mapping_rev.get(pred_sequence, 'Unknown Category')
        seq_tag_name = sequence_tag_mapping_rev.get(pred_seq_tag, 'Unknown Sequence Tag')
        disease_name = disease_label_mapping_rev.get(pred_disease, 'Unknown Disease')
        
        sequence_confidence = round(float(np.max(pred_sequence_probs)) * 100, 2)
        seq_tag_confidence = round(float(np.max(pred_seq_tag_probs)) * 100, 2)
        disease_confidence = round(float(np.max(pred_disease_probs)) * 100, 2)
        
        return {
            "PatientInfo": {
                "Name": str(patient_name),  
                "Sex": patient_sex,
                "Age": patient_age
            },
            "Prediction": {
                "Disease": {
                    "Name": disease_name,
                    "Confidence": f"{disease_confidence}%"
                },
                "Sequence": {
                    "Name": sequence_name,
                    "Confidence": f"{sequence_confidence}%"
                },
                "SequenceTag": {
                    "Name": seq_tag_name,
                    "Confidence": f"{seq_tag_confidence}%"
                }
            }
        }
        
    except Exception as e:
        raise ValueError(f"Error processing {dicom_path}: {e}")

# Protected API endpoint for prediction
@app.route('/predict', methods=['POST'])
@token_required
def predict():
    file = request.files['file']
    temp_image_path = 'temp_image.dcm'
    file.save(temp_image_path)

    try:
        result = predict_and_format(temp_image_path)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Clean up the temporary file
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)

if __name__ == '__main__':
    app.run(debug=True)
