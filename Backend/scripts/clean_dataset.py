
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
