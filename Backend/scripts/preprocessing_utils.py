import cv2
import pydicom
import numpy as np
import os

# Function to check if a file is a valid DICOM
def is_valid_dicom(file_path):
    try:
        pydicom.dcmread(file_path)
        return True
    except pydicom.errors.InvalidDicomError:
        return False

# Function to preprocess a DICOM image or image path
def preprocess_image(input_data, is_dicom=True):
    """
    Preprocess an image from a file path or pixel array.
    If is_dicom=True, expects either a DICOM file path or DICOM pixel array.
    """
    import cv2
    import numpy as np

    if isinstance(input_data, str) and is_dicom:
        # Load DICOM file path using pydicom
        dicom_image = pydicom.dcmread(input_data)
        image = dicom_image.pixel_array
    elif isinstance(input_data, np.ndarray):
        # Input is already a pixel array
        image = input_data
    else:
        raise ValueError("Invalid input data type for DICOM preprocessing.")

    # Example preprocessing (resize, normalize, etc.)
    image = cv2.resize(image, (128, 128))
    image = image / 255.0  # Normalize pixel values

    # Reshape to match the model input if needed
    return image.reshape(1, 128, 128, 1)  # Single image batch format
