import os
import numpy as np
import pydicom
import json
from keras._tf_keras.keras.models import load_model
from preprocessing_utils import preprocess_image  # Ensure this handles DICOM inputs correctly

# Load the trained model and mappings
model_path = 'models/new_trained_multioutput_model.keras'
model = load_model(model_path)

# Load label mappings
with open('models/label_mapping.json', 'r') as f:
    label_mapping = json.load(f)
with open('models/disease_label_mapping.json', 'r') as f:
    disease_label_mapping = json.load(f)
with open('models/sequence_tag_mapping.json', 'r') as f:
    sequence_tag_mapping = json.load(f)

# Reverse mappings for easy interpretation of results
label_mapping_rev = {v: k for k, v in label_mapping.items()}
disease_label_mapping_rev = {v: k for k, v in disease_label_mapping.items()}
sequence_tag_mapping_rev = {v: k for k, v in sequence_tag_mapping.items()}

def predict_on_dicom(dicom_path):
    """Loads, preprocesses, and predicts on a single DICOM image, returning a hierarchical prediction."""
    try:
        # Load DICOM file and extract pixel data
        dicom_image = pydicom.dcmread(dicom_path)
        image = dicom_image.pixel_array
        
        # Preprocess the image (resize, normalize, etc.)
        preprocessed_image = preprocess_image(image, is_dicom=True).reshape(1, 128, 128, 1)
        
        # Make prediction for this single image
        predictions = model.predict(preprocessed_image)
        
        # Extract predicted labels
        pred_sequence = np.argmax(predictions[0], axis=1)[0]
        pred_seq_tag = np.argmax(predictions[1], axis=1)[0]
        pred_disease = np.argmax(predictions[2], axis=1)[0]
        
        # Map predictions to human-readable labels
        sequence_name = label_mapping_rev.get(pred_sequence, 'Unknown Category')
        seq_tag_name = sequence_tag_mapping_rev.get(pred_seq_tag, 'Unknown Sequence Tag')
        disease_name = disease_label_mapping_rev.get(pred_disease, 'Unknown Disease')
        
        # Format output for this single image
        hierarchical_output = {
            disease_name: {
                sequence_name: [seq_tag_name]
            }
        }
        
        return hierarchical_output
    except Exception as e:
        print(f"Error processing file {dicom_path}: {e}")
        return None

def test_model_on_all_files(folder_path):
    """Processes each DICOM image file in a folder individually and outputs hierarchical predictions for each file."""
    all_predictions = {}

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.dcm'):
                dicom_path = os.path.join(root, file)
                print(f"\nProcessing file: {dicom_path}")
                
                # Get hierarchical prediction for each DICOM file
                result = predict_on_dicom(dicom_path)
                
                if result is not None:
                    # Store result in dictionary with file path as key
                    all_predictions[dicom_path] = result

                    # Print result for this individual file
                    print(f"Hierarchical Output for {dicom_path}:")
                    print(json.dumps(result, indent=4))

    # Save all results to JSON
    output_json_path = 'output/prediction_results.json'
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    with open(output_json_path, 'w') as json_file:
        json.dump(all_predictions, json_file, indent=4)
        print(f"\nAll results saved to {output_json_path}")

# Example usage for testing on the entire `data/test` folder
test_folder_path = 'data/test'
test_model_on_all_files(test_folder_path)
