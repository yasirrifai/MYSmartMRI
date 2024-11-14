import os
import pydicom
import cv2
import pandas as pd
import numpy as np
from PIL import Image
import shutil

# Set paths
input_folder = 'data/train'       # Top-level directory with subfolders containing DICOM files
output_csv = 'output/dataset_labels.csv'
output_folder = 'extracted_images'

# Ensure output folder exists
os.makedirs(os.path.join(output_folder, "images"), exist_ok=True)
os.makedirs(os.path.join(output_folder, "sequences"), exist_ok=True)

# Helper function to categorize sequences
def categorize_sequence(sequence_name):
    sequence_name = sequence_name.lower() if isinstance(sequence_name, str) else ""
    if any(key in sequence_name for key in [
        "t1", "tfl", "fl3d1", "tir", "mprage", "spgr", "t1rho", 
        "t1flash", "t1fl3d", "mdeft", "t1space", "t1ir", "t1spin"
    ]):
        return "T1"
    elif any(key in sequence_name for key in [
        "t2", "h2", "t2se", "t2fse", "t2tse", "t2spair", "t2star", 
        "pdw", "t2dir", "t2csi", "t2map", "t2prep", "t2ge", "t2spir", "tse"
    ]):
        return "T2"
    elif any(key in sequence_name for key in [
        "flair", "fl2", "fl3", "irfse", "tir", "tirm", "space", 
        "t2flair", "t2tir", "t2ir", "stir", "flair3d"
    ]):
        return "FLAIR"
    elif any(key in sequence_name for key in [
        "dwi", "dw", "epi", "adc", "diff", "diffusion", "dwi_epi", 
        "tracew", "bval", "trace", "dti", "ep"
    ]):
        return "DWI"
    elif any(key in sequence_name for key in [
        "pd", "proton", "pdw"
    ]):
        return "PD"
    return "UNKNOWN"

# Helper function to save DICOM as image
def save_dicom_as_image(ds, output_path):
    pixel_array = ds.pixel_array
    if pixel_array.ndim == 2:
        img = Image.fromarray(pixel_array)
        img.save(output_path)
    elif pixel_array.ndim == 3:
        for i in range(pixel_array.shape[0]):
            img = Image.fromarray(pixel_array[i])
            img.save(f"{output_path}_slice_{i}.png")

# Prepare the list to hold data for the CSV
data_records = []

# Loop through each subfolder and DICOM file
for root, dirs, files in os.walk(input_folder):
    for file_name in files:
        if file_name.endswith('.dcm') or file_name.endswith('.dicom') or file_name.endswith('.ima'):
            file_path = os.path.join(root, file_name)
            try:
                ds = pydicom.dcmread(file_path)
                sequence_name = ds.get("SequenceName", "UNKNOWN")
                category = categorize_sequence(sequence_name)

                # Extract the main folder name as the Disease Label
                relative_path = os.path.relpath(root, input_folder)
                disease_label = relative_path.split(os.sep)[0]
                
                # Create category folder
                category_folder = os.path.join(output_folder, "sequences", category)
                os.makedirs(category_folder, exist_ok=True)

                # Save the DICOM as a PNG image
                img_output_path = os.path.join(output_folder, "images", f"{os.path.splitext(file_name)[0]}.png")
                save_dicom_as_image(ds, img_output_path)

                # Organize metadata
                # Organize metadata
                data_entry = {
                    'File Path': file_path,
                    'Image Path': img_output_path,
                    'Sequence Name': sequence_name,
                    'Category': category,
                    'Disease Label': disease_label,  
                    'Image Position (Patient)': ds.get((0x0020, 0x0032), '').value if ds.get((0x0020, 0x0032)) else '',
                    'TR': ds.get((0x0018, 0x0080), '').value if ds.get((0x0018, 0x0080)) else '',
                    'TE': ds.get((0x0018, 0x0081), '').value if ds.get((0x0018, 0x0081)) else '',
                    'Slice Thickness': ds.get((0x0018, 0x0050), '').value if ds.get((0x0018, 0x0050)) else '',
                    'Pixel Spacing': ds.get((0x0028, 0x0030), '').value if ds.get((0x0028, 0x0030)) else '',
                    'Study Date': ds.get((0x0008, 0x0020), '').value if ds.get((0x0008, 0x0020)) else '',
                    'Series Date': ds.get((0x0008, 0x0021), '').value if ds.get((0x0008, 0x0021)) else '',
                    'Modality': ds.get((0x0008, 0x0060), '').value if ds.get((0x0008, 0x0060)) else '',
                    'Sequence Name Tag': ds.get((0x0018, 0x0024), '').value if ds.get((0x0018, 0x0024)) else '',
                    'Rescale Slope': ds.get((0x0028, 0x1053), '').value if ds.get((0x0028, 0x1053)) else '',
                    'Rescale Intercept': ds.get((0x0028, 0x1052), '').value if ds.get((0x0028, 0x1052)) else '',
                    'Patient Age': ds.get((0x0010, 0x1010), '').value if ds.get((0x0010, 0x1010)) else '',
                    'Patient Sex': ds.get((0x0010, 0x0040), '').value if ds.get((0x0010, 0x0040)) else '',
                }

                data_records.append(data_entry)

                # Move the file to the respective category folder
                shutil.move(file_path, os.path.join(category_folder, file_name))

            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        else:
            print(f"Skipping non-DICOM file: {file_name}")

# Create and save CSV file
df = pd.DataFrame(data_records)
df.to_csv(output_csv, index=False)
print(f"CSV file created at {output_csv}")
