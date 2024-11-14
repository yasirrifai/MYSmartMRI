import os
import numpy as np
import pandas as pd
import cv2
from tensorflow.keras.models import load_model

# Load the pre-trained CNN model for disease prediction
model = load_model('models/trained_cnn_model.h5')

# Directory of new, unlabeled images
unlabeled_images_path = 'data/test/'
results = []

# Preprocess images for prediction
import pydicom

# Updated image preprocessing function for handling DICOM images
def preprocess_image(image_path, target_size=(128, 128)):
    if image_path.endswith('.dcm'):
        try:
            ds = pydicom.dcmread(image_path)
            image = ds.pixel_array
            if image is not None:
                image = cv2.resize(image, target_size) / 255.0  # Normalize
                image = np.expand_dims(image, axis=-1)  # Add channel dimension for grayscale
                image = np.expand_dims(image, axis=0)   # Add batch dimension
                return image
            else:
                print(f"Warning: Unable to process pixel data from DICOM at {image_path}")
                return None
        except Exception as e:
            print(f"Error reading DICOM file {image_path}: {e}")
            return None
    else:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            image = cv2.resize(image, target_size) / 255.0
            image = np.expand_dims(image, axis=-1)
            image = np.expand_dims(image, axis=0)
            return image
        else:
            print(f"Warning: Unable to load image at {image_path}")
            return None


# Predict and annotate
for filename in os.listdir(unlabeled_images_path):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.dcm'):
        image_path = os.path.join(unlabeled_images_path, filename)
        processed_image = preprocess_image(image_path)
        
        if processed_image is not None:
            prediction = model.predict(processed_image)
            predicted_label = np.argmax(prediction)
            confidence = np.max(prediction)
            
            # Append to results for review
            results.append({
                'Image Path': image_path,
                'Predicted Label': predicted_label,
                'Confidence': confidence
            })
        else:
            print(f"Skipped image at {image_path} due to load issues.")

# Save results to a CSV for verification
results_df = pd.DataFrame(results)
results_df.to_csv('output/automated_annotations.csv', index=False)
print("Automated annotations saved to output/automated_annotations.csv")
