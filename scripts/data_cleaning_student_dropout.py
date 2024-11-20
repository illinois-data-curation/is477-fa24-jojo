import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/student_dropout.csv", sep=";")

# Handle missing values
df['Age at enrollment'].fillna(df['Age at enrollment'].median(), inplace=True)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)

# Standardize column names (e.g., remove extra spaces)
df.columns = df.columns.str.strip()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save the cleaned dataset
df.to_csv("data/cleaned/student_dropout_cleaned.csv", index=False)

print("Student dropout dataset cleaned successfully.")
 