import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/student_performance.csv", sep=";")

# Handle missing values (e.g., fill with median for numerical columns, mode for categorical)
df['age'].fillna(df['age'].median(), inplace=True)  # For numerical columns
df['sex'].fillna(df['sex'].mode()[0], inplace=True)  # For categorical columns

# Standardize column names (e.g., remove extra spaces)
df.columns = df.columns.str.strip()

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save the cleaned dataset
df.to_csv("data/cleaned/student_performance_cleaned.csv", index=False)

print("Student performance dataset cleaned successfully.")
