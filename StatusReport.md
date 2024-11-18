### Task 1: Acquire Datasets from at least Two Sources

**Status:** *Completed (Week 10)*  
**Artifacts:**

- **Data Acquisition Script:** [`scripts/data_acquisition.py`](https://github.com/teamjojo/project/blob/main/scripts/data_acquisition.py)
- **Raw Datasets:**
  - Student Performance Dataset: [`data/raw/student_performance.csv`](https://github.com/teamjojo/project/blob/main/data/raw/student_performance.csv)
  - Predict Students' Dropout Dataset: [`data/raw/student_dropout.csv`](https://github.com/teamjojo/project/blob/main/data/raw/student_dropout.csv)

**Description:**

We successfully acquired the two datasets programmatically using the `data_acquisition.py` script. The script automates the download process and ensures data integrity through SHA-256 checksums. The datasets are stored in the `data/raw/` directory for further processing.

### Task 2: Automatic Integration of Datasets using Python/Pandas and/or SQL

**Status:** *In Progress (Week 11 - Week 12)*  
**Artifacts:**

- **Data Integration Script:** [`scripts/data_integration.py`](https://github.com/teamjojo/project/blob/main/scripts/data_integration.py)
- **Data Integration Plan:** [`docs/data_integration_plan.md`](https://github.com/teamjojo/project/blob/main/docs/data_integration_plan.md)

**Description:**

We analyzed the schemas of both datasets to identify common variables and discrepancies. The integration script merges the datasets based on common keys such as `student_id` and `gender`. Data type mismatches and naming inconsistencies are being handled within the script. The integration plan documents the steps and considerations for merging the datasets.

### Task 3: Transparent Data Profiling, Quality Assessment, and Cleaning

**Status:** *Completed (Week 12)*  
**Artifacts:**

- **Data Profiling Reports:**
  - Student Performance Dataset: [`reports/data_profiling_student_performance.md`](https://github.com/teamjojo/project/blob/main/reports/data_profiling_student_performance.md)
  - Predict Students' Dropout Dataset: [`reports/data_profiling_student_dropout.md`](https://github.com/teamjojo/project/blob/main/reports/data_profiling_student_dropout.md)
- **Data Cleaning Scripts:**
  - Student Performance: [`scripts/data_cleaning_student_performance.py`](https://github.com/teamjojo/project/blob/main/scripts/data_cleaning_student_performance.py)
  - Predict Students' Dropout: [`scripts/data_cleaning_student_dropout.py`](https://github.com/teamjojo/project/blob/main/scripts/data_cleaning_student_dropout.py)
- **Cleaned Datasets:**
  - Student Performance Cleaned: [`data/cleaned/student_performance_cleaned.csv`](https://github.com/teamjojo/project/blob/main/data/cleaned/student_performance_cleaned.csv)
  - Predict Students' Dropout Cleaned: [`data/cleaned/student_dropout_cleaned.csv`](https://github.com/teamjojo/project/blob/main/data/cleaned/student_dropout_cleaned.csv)

**Description:**

Data profiling was conducted using OpenRefine and Python's Pandas library. We assessed data quality, identifying issues such as missing values, outliers, and inconsistent categories. The data cleaning scripts address these issues by:

- Handling missing values through imputation or removal.
- Correcting data entry errors and standardizing categorical variables.
- Removing duplicates to ensure data integrity.

