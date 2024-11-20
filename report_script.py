import pandas as pd

# Load the datasets
student_performance = pd.read_csv("data/raw/student_performance.csv", sep=";")
student_dropout = pd.read_csv("data/raw/student_dropout.csv", sep=";")

# Generate basic profile for the student performance dataset
performance_profile = student_performance.describe(include='all')
performance_profile.to_markdown("reports/data_profiling_student_performance.md")

# Generate basic profile for the student dropout dataset
dropout_profile = student_dropout.describe(include='all')
dropout_profile.to_markdown("reports/data_profiling_student_dropout.md")
 