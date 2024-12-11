import os 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset 
student_path = "final_project/is477-fa24-jojo/data/integrated_data/students.csv" # or data/~ after cd "is477-fa24-jojo"
df = pd.read_csv(student_path)

# print(df.groupby(['sex']).describe())

# # Define the parent directory for image/figures 
# base_directory = 'final_project/is477-fa24-jojo'
# parent_directory = os.path.join(base_directory, 'figures')
# if not os.path.exists(parent_directory):
#     os.makedirs(parent_directory, exist_ok=True)

# file_name = 'association_sex&final_grade.png'
# file_path = os.path.join(parent_directory, file_name)

# # Save the cleaned DataFrame to the new directory
# plt.savefig(file_path, index=False)

# print(f"association figure is saved to {file_path}")
print(df.dtypes)
# df_fem = df[df['sex'] == 1]
# df_mal = df[df['sex'] == 2]


# Calculate correlation matrix without two columns that have objects 
# df2 = df.loc[:, ~df.columns.isin(['Pstatus', 'school'])]
# corr_matrix = df2.corr()

# # Create heatmap
# plt.figure(figsize=(12, 10))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
# plt.title('Correlation Heatmap of Variables')
# plt.show()
