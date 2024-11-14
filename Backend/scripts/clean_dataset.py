# import pandas as pd

# # Load CSV
# csv_path = 'output/cleaned_dataset_labels.csv'
# df = pd.read_csv(csv_path)

# # Print unique values for both columns to check consistency
# print("Unique sequence labels in CSV:", df['Category'].unique())
# print("Unique disease labels in CSV:", df['Disease Label'].unique())

# # Create label mappings based on the unique values found in the CSV
# label_mapping = {label: idx for idx, label in enumerate(df['Category'].unique())}
# disease_label_mapping = {label: idx for idx, label in enumerate(df['Disease Label'].unique())}

# print("\nGenerated label mapping for sequences:")
# for key, val in label_mapping.items():
#     print(f"{key}: {val}")

# print("\nGenerated label mapping for diseases:")
# for key, val in disease_label_mapping.items():
#     print(f"{key}: {val}")

# # Validate data for missing or incorrect labels
# missing_sequences = df['Category'].isnull().sum()
# missing_diseases = df['Disease Label'].isnull().sum()

# if missing_sequences > 0 or missing_diseases > 0:
#     print(f"\nWarning: Found {missing_sequences} missing sequence labels and {missing_diseases} missing disease labels.")
# else:
#     print("\nNo missing labels found.")

# # Ensure there are no discrepancies between labels and mappings
# sequence_classes = len(label_mapping)
# disease_classes = len(disease_label_mapping)

# print(f"\nNumber of unique sequence classes: {sequence_classes}")
# print(f"Number of unique disease classes: {disease_classes}")

# # Check for mismatches in one-hot encoding
# print("\nChecking one-hot encoding compatibility...")
# if 'Category' in df.columns and 'Disease Label' in df.columns:
#     num_sequence_classes = len(label_mapping)
#     num_disease_classes = len(disease_label_mapping)

#     if num_sequence_classes != num_disease_classes:
#         print("Warning: The number of sequence classes and disease classes do not match.")
#     else:
#         print("The number of sequence classes matches the number of disease classes.")
# else:
#     print("Error: Required columns ('Category' and 'Disease Label') not found in CSV.")

# # Save a cleaned version of the CSV (optional)
# cleaned_csv_path = 'output/cleaned_dataset_labels.csv'
# df.to_csv(cleaned_csv_path, index=False)
# print(f"\nCleaned CSV saved at: {cleaned_csv_path}")

import pandas as pd

# Load the CSV file
csv_path = 'output/dataset_labels.csv'  # Path to your CSV file
df = pd.read_csv(csv_path)

# Select only the relevant columns
selected_columns = ['Image Path', 'Category', 'Sequence Name Tag', 'Disease Label']
df_filtered = df[selected_columns]

# Remove duplicates to get unique rows
df_unique = df_filtered.drop_duplicates()

# Check for missing values and handle them if necessary
df_unique.fillna('UNKNOWN', inplace=True)

# Save the filtered data to a new CSV file
output_csv_path = 'unique_image_data.csv'
df_unique.to_csv(output_csv_path, index=False)

print(f"Filtered data saved to {output_csv_path}")
