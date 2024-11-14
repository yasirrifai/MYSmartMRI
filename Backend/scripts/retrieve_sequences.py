import pandas as pd

# Load CSV file
csv_path = 'output/dataset_labels.csv'  # Replace with your actual path
df = pd.read_csv(csv_path)

# Check if 'Sequence Name Tag' column exists
if 'Sequence Name Tag' in df.columns:
    # Get unique values in 'Sequence Name Tag' column
    unique_sequence_tags = df['Sequence Name Tag'].unique()
    
    # Print unique values
    print("Unique records in 'Sequence Name Tag' column:")
    for tag in unique_sequence_tags:
        print(tag)
else:
    print("The column 'Sequence Name Tag' was not found in the CSV file.")
