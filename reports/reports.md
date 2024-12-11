## Environment Set up
We created a virtual python environment that includes all the necessary libraries for this project. The details are in [environment.md](../setup/environment.md). 

## Data Importation 
We picked our datasets both from the UCI Machine Learning Repository website.
- [highschool student dataset](https://archive.ics.uci.edu/dataset/320/student+performance): Cortez, Paulo. "Student Performance." UCI Machine Learning Repository, 2008, https://doi.org/10.24432/C5TG7T.
- [college student dataset](https://archive.ics.uci.edu/dataset/856/higher+education+students+performance+evaluation): Yilmaz, Nevriye and Boran Şekeroğlu. "Higher Education Students Performance Evaluation." UCI Machine Learning Repository, 2019, https://doi.org/10.24432/C51G82.

**1. Student Performance** 
<br>
This dataset is created to predict student performance in secondary education (high school). The data attributes were collected by using school reports and questionnaires from secondary educations of two Portuguese schools. The datasets provide performance in two subjects: mathematics (mat) and portugues language (por). We decided to obtain these datasets combined from pip installing the ucirepo from the requirements.txt for the reproducibility purpose. The target variables are G1, G2, and G3. Each represents grades from each period of school year; G3 represents the final grade, meaning it's the output target. 

* Feature dataset 
<br>
It has 649 rows x 30 columns. 
* Target dataset
<br>
It includes the same number of rows (649) but 3 columns which are the grades over 3 time periods. 
    - G1 
    - G2
    - G3: final grade 

>[importing this dataset](../scripts/highschool_data_import.py)

**2. Higher Education Students Performance Evaluation**
<br>
The data was collected from the Faculty of Engineering and Faculty of Educational Sciences students in 2019. 
It has 145 rows x 31 columns.
**need more details about the original dataset itself**

## Data Pre-Processing 
### High School Data 
>[highschool_data_import.py](../scripts/highschool_data_import.py)

The script fetches a dataset on student performance in secondary education using the UCI Machine Learning Repository.

**Feature Selection and Renaming:**
- Selected features include: age, sex, activities, romantic status, parents' education, parental status, and study time.
- A new column "school" is added with the value "highschool" to identify the data source.

**Data Transformations:**
- Age is converted to categories (0: <18, 1: 18-21, 2: 22+).
- Sex is encoded numerically (1: female, 2: male).
- Romantic status is encoded (1: yes, 2: no).
- Activities are converted to integer values (1: yes, 2: no).

**Target Variable:**
- The final grade (G3) is converted to a letter grade scale (0-7) for the high school grading system to match the college grading scale, allowing for unified analysis.

### College Data 
>[college_data_import.py](../scripts/college_data_import.py)

This script imports data on higher education students' performance evaluation.

**Feature Selection and Renaming:**
- Similar features to the high school dataset are selected and renamed for consistency.
- A "school" column is added with the value "college".

**Data Transformations:**
- Parents' education levels are standardized (1-4 scale) by replacing 5 & 6 (masters & Ph.D) with 4 (higher education).
- Parental status is converted to binary (T: together, A: apart).
- Study time categories are adjusted to match the high school dataset.

## Data Integration
>[data_integration.py](../scripts/data_integration.py)

This script combines the preprocessed high school and college datasets.

**Process:**
1. Loads the cleaned datasets from their respective CSV files.
2. Concatenates the two datasets into a single DataFrame.
3. Saves the integrated dataset as 'students.csv' in the 'integrated_data' directory.

## Data Acquisition
>[data_acquisition.py](../scripts/data_acquisition.py)

This script checks if the datasets exist in the correct location. 

## Data Analysis 
>[data_analysis.py](../scripts/data_analysis.py)

This script performs initial exploratory data analysis on the integrated dataset.

**Analysis Steps:**
1. Loads the integrated 'students.csv' file.
2. Prints the data types of all columns.
3. Contains commented-out code for:
   - Grouping data by sex and generating descriptive statistics.
   - Creating a correlation heatmap **(currently commented out**).

**Analysis Result:** 
<br>
explain the heatmap result 

**Recommendations for Further Analysis**
1. Conduct comparative analyses between high school and college students.
2. Investigate the impact of socio-economic factors (parents' education, parental status) on academic performance.
3. Explore the relationship between extracurricular activities and academic outcomes.
4. Consider implementing machine learning models to predict student performance based on the available features.

## Data Visualization
>![correlation_heatmap_female](figures/heatmap_female.png)

>![correlation_heatmap_male](figures/heatmap_male.png)
insert visualization image by the call out code and interpret the visualization a little bit. 

## Reproducing 

