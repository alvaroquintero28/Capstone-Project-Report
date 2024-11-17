## Instructions for Managing the Project Virtual Environment

Following instructions for managing the virtual environment for the Capstone-Project-Report, including steps for creating, activating, and installing required dependencies.

### 1. Create the Virtual Environment

In the project root directory, run the following command to create a virtual environment named `venv`:

```python
python -m venv .venv
```
This command will create a new directory called venv, which will contain all the necessary files for the virtual environment.

### 2. Activate the Project Virtual Environment
```python
source venv/bin/activate
```

### 3. Install Dependencies
Install dependencies into your `.venv` 
pip install pandas seaborn matplotlib

### Command to generate a requirements.txt with all installed packages
pip freeze > requirements.txt

# Stroke Prediction Capstone Project

**Author:** Alvaro Quintero Gonzalez  
**Institution:** Northwest Missouri State University, Maryville MO 64468, USA  
**Email:** [S573928@nwmissouri.edu](mailto:S573928@nwmissouri.edu) and [alvaroquintero28@yahoo.com](mailto:alvaroquintero28@yahoo.com)  

## Abstract
Stroke prediction is a critical area of research in healthcare, aiming to enhance preventative strategies and improve patient outcomes. This study investigates a comprehensive dataset collected from various healthcare sources, consisting of demographic, clinical, and lifestyle factors associated with stroke risk. The dataset encompasses attributes such as age, gender, blood pressure, cholesterol levels, body mass index (BMI), and lifestyle habits. "Will finish at completion"

**Keywords:** Stroke Prediction, Preventative Strategies, Demographic Factors, Predictive Modeling, Machine Learning Algorithms

## Introduction
Strokes are a major health concern globally, recognized as one of the leading causes of disability and death. Occurring when blood flow to the brain is disrupted, it can lead to significant physical, cognitive, and emotional impairments in affected individuals. The impact of strokes extends beyond the individual, affecting families and communities, and placing a substantial strain on healthcare systems. With the rising incidence of strokes associated with aging populations and the increasing prevalence of risk factors such as hypertension, obesity, and diabetes, there is an urgent need to focus on effective stroke prevention strategies. 

Prevention requires a multifaceted approach that includes public education, early identification of risk factors, and lifestyle modifications. Simple changes, such as adopting a balanced diet, engaging in regular physical activity, and managing underlying health conditions, can greatly reduce an individual's risk of stroke. Moreover, healthcare providers must play an active role in raising awareness about stroke prevention and ensuring that at-risk patients receive appropriate screenings and interventions. By promoting a comprehensive understanding of stroke risk factors, we can empower individuals to take charge of their health. This proactive approach not only aims to reduce the frequency of strokes but also facilitates overall public health awareness, fostering healthier communities. As advances in knowledge and strategies for stroke prevention, we can work towards a future where strokes are less frequent and their consequences are minimized.

### Define the Problem and Goals of This Capstone Project
This section discusses the goals of the proposed project. The primary focus of this capstone project is to develop a comprehensive understanding of stroke prediction and prevention strategies using data-driven approaches. The main goal consists of identifying key risk factors. By applying statistical analysis and machine learning techniques, it will determine which variables are most predictive of stroke occurrence. Further focus will evaluate the performance of developed models in predicting stroke events, thereby providing valuable insights for early intervention. The project will propose targeted preventive strategies that can be implemented in community health programs, enhancing greater public awareness.

#### Project Links
Key resources for this project provided below:

- [Capstone-Project-Report GitHub](https://github.com/alvaroquintero28/Capstone-Project-Report)
- [Capstone Project Report Overleaf](https://es.overleaf.com/read/zqgzcfntnwbz#9bc8ce)

### The Following Are the Phases of Project Implementation
1. Define the Problem and Objectives
   - Clearly articulate the specific questions and objectives of the analysis, focusing on how heart disease predictions can improve preventive measures for stroke patients.
   - Identify key performance indicators (KPIs) to measure the success of the project.
   
2. Literature Review and Background Research
   - Conduct a thorough review of existing literature on heart disease, stroke rehabilitation, and predictive analytics in healthcare.
   - Gather insights into current best practices and identify gaps in the existing research that your project can address.

3. Data Collection
   - Search for relevant datasets using the identified sources (e.g., ProjectPro, American Journal of Medicine) focusing on:
     - Patient demographics
     - Medical history related to heart disease and strokes
     - Lifestyle factors (e.g., diet, exercise)
     - Laboratory test results (e.g., cholesterol levels, blood pressure)
   - Ensure that the data is reliable, accurate, and representative of the population you wish to study.

4. Data Pre-processing
   - Clean the data by handling missing values, outliers, and inconsistencies.
   - Perform data normalization or standardization if necessary.
   - Encode categorical variables to facilitate analysis in machine learning models.

5. Exploratory Data Analysis (EDA)
   - Analyze the dataset to uncover patterns and relationships between variables.
   - Use visualizations (graphs, plots) to represent findings and identify key risk factors associated with heart disease in stroke patients.
   - Identify and select the most relevant features that influence heart disease predictions.
   - Use techniques like correlation analysis, recursive feature elimination (RFE), or machine learning algorithms to enhance feature selection.

6. Model Development
   - Choose appropriate machine learning models for prediction:
     - Logistic Regression
     - Decision Trees
     - Random Forest
     - Support Vector Machines
     - Neural Networks
   - Split the dataset into training and testing sets for model evaluation.
   - Train the selected models on the training dataset.
   - Optimize model performance using techniques like hyperparameter tuning and cross-validation to prevent overfitting.
   - Assess the accuracy and effectiveness of the models using the testing dataset.
   - Use evaluation metrics such as accuracy, precision, recall, F1 score, and the ROC-AUC curve to measure performance.
   - Compare the performance of different models to select the best one.

7. Conclusion
   - Interpret results:
     - Analyze the results of the best-performing model to understand the impact of various factors on heart disease predictions.
     - Provide actionable insights and recommendations for preventing heart disease in stroke patients based on the findings.
   - Discussion of the limitations.
   - Ideas for future work.

## Literature Review and Background Research
Numerous studies have identified effective preventive measures for reducing the risk of stroke, emphasizing both management of hypertension and lifestyle interventions. Hypertension is the most significant modifiable risk factor for stroke, and studies have shown that controlling blood pressure through lifestyle changes, such as a healthy diet, regular physical activity, reducing sodium intake, smoking cessation, and adhering to prescribed antihypertensive medications can significantly lower the likelihood of experiencing a stroke. 

Maintaining blood pressure within a normal range (typically less than 120/80 mmHg) is crucial in preventing both ischemic and hemorrhagic strokes, making it the most critical focus in stroke prevention efforts. Combined, these research findings underscore the importance of a multifaceted approach to stroke prevention that integrates medical treatment with proactive lifestyle changes.

### Limitations
The healthcare stroke prevention dataset and the well-being and lifestyle dataset each have inherent limitations that may affect the comprehensiveness and applicability of their findings. Firstly, the stroke prevention dataset may suffer from issues related to sample size and demographic representation, potentially limiting the generalizability of the results across diverse populations. Additionally, the accuracy of self-reported data regarding lifestyle factors in the well-being and lifestyle dataset may be compromised by social desirability bias, where participants might under-report unhealthy behaviors or exaggerate healthy ones. Furthermore, the transient nature of lifestyle habits makes it challenging to capture accurate and stable data over time, potentially leading to discrepancies in understanding long-term behavior trends.

## Data
Data collection for this analysis involved two comprehensive datasets sourced from Kaggle: the Wellbeing and Lifestyle Data and the Healthcare Dataset on Stroke Data. The Wellbeing and Lifestyle Data dataset encompasses a variety of factors influencing individual health and well-being, such as lifestyle choices. It features demographic information, including age, gender, and socioeconomic status, facilitating an understanding of how these variables correlate with reported well-being outcomes. The Healthcare Dataset and Stroke Data, on the other hand, presents critical health metrics and conditions related to stroke incidents among patients. By merging insights from these two datasets, a more comprehensive picture of lifestyle influences on health outcomes can be constructed, enabling a deeper exploration of the relationships between well-being, lifestyle choices, and stroke risk.

### Dataset Variable Attributes
The following tables summarize the original data attributes, including their descriptions, data types, and possible values prior to any data cleaning. These attributes are essential for understanding the collected data and are crucial for any subsequent analysis.

#### Attributes, Descriptions, and Possible Values from Healthcare Dataset

| Attribute          | Description                                                      | Possible Values                                        |
|--------------------|------------------------------------------------------------------|-------------------------------------------------------|
| **id**             | Unique identifier for each patient                              | Whole numbers                                          |
| **gender**         | Gender of the patient                                            | "Male", "Female", "Other"                            |
| **age**            | Age of the patient in years                                      | Whole numbers (e.g., 0, 1, 25, 60)                   |
| **hypertension**   | Indicates if the patient has hypertension                        | 0 (No), 1 (Yes)                                      |
| **heart_disease**  | Indicates if the patient has heart disease                       | 0 (No), 1 (Yes)                                      |
| **ever_married**   | Indicates if the patient has ever been married                   | "Yes", "No"                                          |
| **work_type**      | Type of employment of the patient                                | "Children", "Govt job", "Self-employed", "Private", "Never worked" |
| **Residence_type** | Type of residence of the patient                                 | "Urban", "Rural"                                     |
| **avg_glucose_level** | Average glucose level of the patient                          | Positive floats (e.g., 70.0, 220.0)                  |
| **bmi**            | Body Mass Index of the patient                                   | Positive floats (e.g., 18.5, 30.0) or "N/A"          |
| **smoking_status** | Indicates the smoking status of the patient                      | "formerly smoked", "smokes", "never smoked", "Unknown" |
| **stroke**         | Indicates if the patient has had a stroke                       | 0 (No), 1 (Yes)                                      |

#### Attributes, Descriptions, and Possible Values from Work-Life Balance Dataset

| Attribute                 | Description                                                | Possible Values                                        |
|---------------------------|----------------------------------------------------------|-------------------------------------------------------|
| **Timestamp**             | Date of the record entry                                 | Date format (e.g., "7/7/15")                         |
| **FRUITS_VEGGIES**       | Number of servings of fruits and vegetables consumed daily | Whole numbers (e.g., 0, 1, 2, 10)                   |
| **DAILY_STRESS**         | Daily stress level rating                                 | Whole numbers (e.g., 1 to 10)                         |
| **PLACES_VISITED**       | Number of places visited daily                            | Whole numbers (e.g., 0, 1, 2, 10)                   |
| **CORE_CIRCLE**          | Number of close relationships or friends                  | Whole numbers (e.g., 0, 1, 8)                        |
| **SUPPORTING_OTHERS**    | Amount of time spent supporting others                   | Whole numbers (e.g., 0, 1, 10)                       |
| **SOCIAL_NETWORK**       | Size of social network measured as a rating               | Whole numbers (e.g., 0 to 10)                        |
| **ACHIEVEMENT**          | Personal achievements reported                             | Whole numbers (e.g., 0 to 10)                        |
| **DONATION**             | Amount donated in a monitored period                      | Whole numbers (e.g., 0, 1, 100)                      |
| **BMI_RANGE**            | Body Mass Index range category                             | "Less than 20", "21 to 35", "36 to 50", "51 or more"|
| **TODO_COMPLETED**       | Number of to-do tasks completed                           | Whole numbers (e.g., 0, 1, 5)                        |
| **FLOW**                 | Flow state engagement score                               | Whole numbers (e.g., 0 to 10)                        |
| **DAILY_STEPS**          | Number of steps taken daily                               | Whole numbers (e.g., 0, 1000, 10000)                   |
| **LIVE_VISION**          | Level of clarity regarding personal goals                  | Whole numbers (e.g., 0 to 10)                        |
| **SLEEP_HOURS**          | Average hours of sleep per night                          | Whole numbers (e.g., 0, 5, 8)                        |
| **LOST_VACATION**        | Indicates if vacation days were unused                    | 0 (No), 1 (Yes)                                      |
| **DAILY_SHOUTING**       | Number of times shouted in a day                          | Whole numbers (e.g., 0, 1, 5)                        |
| **SUFFICIENT_INCOME**    | Indicates if income is sufficient                         | 0 (No), 1 (Yes)                                      |
| **PERSONAL_AWARDS**      | Number of personal awards received                        | Whole numbers (e.g., 0, 2, 10)                       |
| **TIME_FOR_PASSION**      | Amount of time available for personal passions           | Whole numbers (e.g., 0, 1, 10)                       |
| **WEEKLY_MEDITATION**    | Hours spent meditating each week                         | Whole numbers (e.g., 0, 1, 5)                        |
| **AGE**                  | Age category of the individual                            | "Less than 20", "21 to 35", "36 to 50", "51 or more"|
| **GENDER**               | Gender of the individual                                  | "Male", "Female"                                     |
| **WORK_LIFE_BALANCE_SCORE**| Score representing work-life balance                    | Float numbers                                         |

## Cleaning
Data cleaning was a crucial step in preparing the datasets for analysis, ensuring they were accurate, consistent, and complete. This update involved cleaning and consolidating attributes from various sources, namely the original healthcare dataset and the work-life balance survey. Such extensive data cleaning was essential for addressing the research question about the relationships between health conditions, demographic factors, and work-life balance. 

During the cleaning process, inconsistencies in categorical variables were identified and rectified. For instance, gender data were standardized for consistency. The following code snippet illustrates this process:

```python
df['gender'] = df['gender'].str.lower().replace({'female': 'F', 'male': 'M'})
# Stroke Prediction Capstone ProjectAdditionally, health conditions such as hypertension and heart disease were encoded as binary values (0 for "No" and 1 for "Yes") to enhance reliability:
df['hypertension'] = df['hypertension'].replace({'No': 0, 'Yes': 1}) 
df['heart disease'] = df['heart disease'].replace({'No': 0, 'Yes': 1})
Numerical data like Body Mass Index (BMI) and income sufficiency scores were rigorously examined. Outliers in continuous variables, including daily stress levels and sleep hours, were identified using Z-score analysis:
from scipy import stats 
df['stress z'] = stats.zscore(df['daily stress']) 
outliers = df[abs(df['stress z']) > 3]
This approach allowed for careful evaluation of outliers, enhancing our understanding of the dataset's validity. Demographic distributions were also analyzed to ensure they matched expected values from the source population. For example, we visualized age distribution through a histogram:
import matplotlib.pyplot as plt 
plt.hist(df['age'], bins=10, edgecolor='black') 
plt.title('Age Distribution') 
plt.xlabel('Age') 
plt.ylabel('Frequency') 
plt.show()
This visualization confirmed that the age distribution accurately reflected the target population, bolstering our findings' external validity. As a result of these data cleaning efforts, we created comprehensive tables that clarified essential variables, such as age, gender, income sufficiency, and sleep hours. These cleaned tables improved data accessibility and understanding across various domains.In this analysis, independent variables included demographic factors (age, gender, income sufficiency) and health conditions (hypertension, heart disease). The dependent variables consisted of health outcomes (stress levels, overall well-being) and lifestyle indicators (sleep hours, work-life balance). This framework enabled us to investigate how independent variables influenced the dependent ones, establishing a solid foundation for further analysis. Ultimately, the streamlined presentation of cleaned data provided a unified perspective on factors affecting health and work-life balance. By clarifying relationships among the variables, the data cleaning process enhanced the potential for robust analysis, facilitating deeper exploration of how various factors impact individuals' health and quality of life.

Work-Life Balance Survey

The data cleaning process for the Work-Life Balance Survey dataset began with an assessment of its initial structure, where the dataset's information and the first few rows are inspected to understand its layout and the types of data contained within. This foundational step allowed for the identification of any discrepancies in column names, which were then standardized by stripping any leading or trailing whitespace.To focus the analysis, only relevant columns—specifically 'DAILY STRESS', 'AGE', 'GENDER', 'INCOME', and 'SLEEP HOURS'—are selected, ensuring that they existed within the DataFrame. Particular attention was given to categorical values; for instance, the age category "Less than 20" is revised to "20 or less" for consistency.Critical numeric conversions were performed on the 'DAILY STRESS' and 'SLEEP HOURS' columns, with errors handled through coercion to address any non-numeric values. Duplicate entries were eliminated to maintain data integrity, followed by a thorough check for missing values across the dataset. Rows with missing data in essential variables were dropped to ensure the robustness of the analysis.

Finally, descriptive statistics were generated to provide insights into the data distribution, and the cleaned dataset was saved as a CSV file, ensuring it is ready for future exploratory analysis. This meticulous cleaning procedure set the groundwork for a comprehensive understanding of the factors influencing work-life balance and contributed to enhanced decision-making regarding employee well-being.

Dataset Cleaning Code and Variable Attributes

The following code and table summarize the cleaned data attributes, including their descriptions, data types, and possible values.

Summary of cleaning code for Work-life Balance Survey

Attributes, Descriptions, and Possible Values from Work-Life Balance SurveyAttributeDescriptionPossible ValuesDAILY_STRESSPerceived daily stress levelWhole numbers (e.g., 1, 2, 3, 4, 5)AGEAge group of respondents"20 or less", "21 to 35", "36 to 50", "51 or more"GENDERGender of respondents"Male", "Female", "Other"SUFFICIENT_INCOMEIndicates if the income is sufficient0 (No), 1 (Yes)SLEEP_HOURSAverage hours of sleep per nightWhole numbers (e.g., 4, 5, 6, 7, 8, 9)