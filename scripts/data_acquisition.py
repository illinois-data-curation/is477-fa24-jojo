import os
import pandas as pd

# Define file paths for datasets
datasets = {
    "student_performance": "data/raw/student_performance.csv",
    "student_dropout": "data/raw/student_dropout.csv"
}

# Ensure the datasets exist in the correct location
for name, file_path in datasets.items():
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Required dataset not found: {file_path}")
    else:
        print(f"Dataset verified: {file_path}")

# Verify and load datasets
def load_dataset(file_path):
    print(f"Loading dataset: {file_path}")
    data = pd.read_csv(file_path)
    print(data.head())
    return data

# Load the datasets for further processing
student_performance_data = load_dataset(datasets["student_performance"])
student_dropout_data = load_dataset(datasets["student_dropout"])
