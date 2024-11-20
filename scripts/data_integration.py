import pandas as pd
import os

# Paths to the datasets
student_performance_path = "data/raw/student_performance.csv"
student_dropout_path = "data/raw/student_dropout.csv"
output_dir = "data/integrated"
output_path = os.path.join(output_dir, "student_data_combined.csv")

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load datasets with correct delimiter
print("Loading datasets...")
student_performance = pd.read_csv(student_performance_path, sep=";")
student_dropout = pd.read_csv(student_dropout_path, sep=";")

# Display column names for verification
print("Columns in student_performance:", student_performance.columns)
print("Columns in student_dropout:", student_dropout.columns)

# Rename columns to unify keys
# Adjust these mappings based on actual column names in the datasets
student_performance.rename(columns={"school": "student_id", "sex": "gender"}, inplace=True)
student_dropout.rename(columns={"Gender": "gender"}, inplace=True)

# Create a unique identifier if "student_id" does not exist
if "student_id" not in student_performance.columns:
    print("'student_id' not found in student_performance; creating unique IDs...")
    student_performance["student_id"] = student_performance.index.astype(str)

if "student_id" not in student_dropout.columns:
    print("'student_id' not found in student_dropout; creating unique IDs...")
    student_dropout["student_id"] = student_dropout.index.astype(str)

# Ensure that the "gender" columns in both datasets have the same data type
student_performance["gender"] = student_performance["gender"].astype(str)
student_dropout["gender"] = student_dropout["gender"].astype(str)

# Merge datasets on common keys (adjust keys as needed)
print("Merging datasets...")
merged_data = pd.merge(
    student_performance, student_dropout, 
    on=["student_id", "gender"], 
    how="inner"  # Choose join type: inner, left, right, outer
)

# Save the merged data to a CSV file
print("Saving merged dataset...")
merged_data.to_csv(output_path, index=False)
print(f"Merged data saved to {output_path}")
 