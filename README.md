# week-3

Sure! Here’s a detailed README.md for all Tasks, including a single markdown that clearly explains the work done for Tasks of my project.

# Insurance Analytics - Task 1: Exploratory Data Analysis (EDA)

## Project Overview

This project is part of the AlphaCare Insurance Solutions (ACIS) analytics initiative aimed at understanding and optimizing insurance business operations. The focus is on historical insurance data to uncover patterns and insights that can enhance customer targeting, improve marketing strategies, and minimize risk. 

Task 1 involves conducting an Exploratory Data Analysis (EDA) on the given dataset to derive key insights about insurance policies, claims, premiums, and other attributes.

---

## Dataset Overview

The dataset contains insurance-related information with the following columns:

- **UnderwrittenCoverID**: A unique identifier for each insurance policy.
- **PolicyID**: A unique identifier for each policyholder.
- **TransactionMonth**: The date of the transaction.
- **IsVATRegistered**: Indicates whether the policyholder is VAT registered.
- **Citizenship**: The citizenship of the policyholder.
- **LegalType**: The legal status of the entity (e.g., Close Corporation, Sole Proprietorship).
- **Title**: The title of the policyholder (e.g., Mr., Ms.).
- **Language**: The preferred language of the policyholder.
- **Bank**: The bank associated with the policyholder.
- **AccountType**: The type of bank account (e.g., Current, Savings).
- **MaritalStatus**: The marital status of the policyholder.
- **Gender**: The gender of the policyholder.
- **Country, Province, PostalCode**: Geographic location of the policyholder.
- **MainCrestaZone, SubCrestaZone**: Geographical zones for insurance risk categorization.
- **ItemType**: Type of item insured (e.g., Mobility - Motor).
- **VehicleType, Make, Model, Cylinders**: Details about insured vehicles (if applicable).
- **SumInsured**: The total sum insured under the policy.
- **CalculatedPremiumPerTerm**: The premium amount paid for the insurance term.
- **TotalPremium, TotalClaims**: The total premiums paid and total claims made by the policyholder.

---

## Objective

The goal of Task 1 is to:
1. Summarize the dataset and provide descriptive statistics.
2. Perform data quality assessment (checking for missing values, data types, and potential outliers).
3. Conduct univariate, bivariate, and multivariate analysis to uncover trends, correlations, and distributions.
4. Visualize key insights to aid in decision-making.
5. Prepare the data for subsequent tasks.

---

## Steps in Task 1

1. Data Loading

We start by loading the dataset into a Pandas DataFrame for analysis. The dataset was provided in a `.txt` file format.

import pandas as pd

Load the dataset
df = pd.read_csv("data/MachineLearningRating_v3.txt", delimiter="|", low_memory=False) 

2. Data Summarization:

 We use descriptive statistics to get an initial understanding of the dataset, including numerical features like TotalPremium, TotalClaims, and categorical variables such as Citizenship, LegalType, and VehicleType.

Data summary
print(df.describe(include='all')) 

3. Data Quality Assessment

 Missing Values: We check for missing values to assess data quality. 

 Data Types: Review the data types of each column and ensure proper formatting (e.g., categorical variables, date columns). 
 
 Outliers: Detect outliers using box plots, particularly for TotalPremium and TotalClaims.

Check for missing values
print(df.isnull().sum())

Check data types
print(df.dtypes) 

4. Univariate Analysis:

 We explore the distribution of individual variables using Histograms for numerical columns like SumInsured, TotalPremium, and TotalClaims. Bar charts for categorical variables like Citizenship, VehicleType, and LegalType.

import matplotlib.pyplot as plt

Plot histogram for TotalPremium
df['TotalPremium'].hist(bins=50) plt.title('Distribution of TotalPremium') plt.xlabel('TotalPremium') plt.ylabel('Frequency') plt.show()

Plot bar chart for Citizenship
df['Citizenship'].value_counts().plot(kind='bar') plt.title('Citizenship Distribution') plt.xlabel('Citizenship') plt.ylabel('Count') plt.show() 

5. Bivariate and Multivariate Analysis:

 We explore relationships between key variables, such as TotalPremium vs TotalClaims, using:

Scatter plots to visualize correlations. Correlation matrix to quantify the strength of relationships between numerical variables.

Scatter plot for TotalPremium vs TotalClaims
df.plot.scatter(x='TotalPremium', y='TotalClaims') plt.title('TotalPremium vs TotalClaims') plt.show()

Correlation matrix
correlation_matrix = df.corr() print(correlation_matrix) 

6. Outlier Detection:

 We use box plots to detect outliers in numerical features, especially focusing on TotalPremium and TotalClaims.

Box plot for TotalPremium
df.boxplot(column='TotalPremium') plt.title('Box Plot for TotalPremium') plt.show() 

7. Data Visualization:

 Three creative and meaningful visualizations were developed:

Distribution of TotalPremium. 

Citizenship Distribution. 

Correlation heatmap for numerical features. 

## Key Findings 

Missing Values: Certain fields, like Citizenship and PostalCode, have missing values, which need to be addressed. 

Outliers: Significant outliers were detected in TotalPremium and TotalClaims. 

Correlations: There is a positive correlation between TotalPremium and TotalClaims, indicating that higher premiums are associated with more claims. 

Data Distribution: The distribution of TotalPremium is heavily skewed, suggesting the need for transformation or handling in future tasks.

# Task 2: Data Version Control (DVC) Setup
 ## Objective
  The objective of Task 2 is to set up Data Version Control (DVC) for tracking data versions, enabling reproducibility of analysis, and ensuring proper management of data and model files.

## Steps in Task 2 DVC Installation:

Installed DVC using the following command:

pip install dvc

Initializing DVC in the Project:

Initialized DVC in the project directory to set up version control for data files:

dvc init Tracking Data with DVC:

Added the data files to be tracked by DVC:

dvc add data/MachineLearningRating_v3.txt This step creates .dvc files that record metadata about the tracked data files.

Storing Data Remotely:

Configured a remote storage location (e.g., S3, GDrive, or a local folder) to store large datasets:

dvc remote add -d myremote /path/to/remote/storage dvc push This allows the team to store the dataset remotely and access it by pulling the latest version when needed.

Data Versioning:

Once the data is versioned, any changes or updates to the dataset are tracked by DVC. To check the status and re-run pipelines after modifying data:

dvc status dvc repro

Pushing DVC Changes:

After adding new data or modifying existing data, push the changes to the remote storage:

dvc push

Collaborating with DVC:

Team members can pull the latest version of the dataset for analysis:

dvc pull

# Task 3: A/B Hypothesis Testing

Perform A/B hypothesis testing on different categorical features to evaluate risk and profit differences. Accept or reject null hypotheses based on statistical significance (p-value < 0.05). Provide insights to help AlphaCare Insurance Solutions make data-driven decisions regarding pricing and risk management. 

## Hypotheses Tested

1. Risk Differences Across Provinces (TotalClaims) Null Hypothesis (H₀): There is no risk difference between provinces. Alternative Hypothesis (H₁): There is a significant risk difference between provinces.
2. Risk Differences Between Zip Codes (TotalClaims) Null Hypothesis (H₀): There is no risk difference between zip codes. Alternative Hypothesis (H₁): There is a significant risk difference between zip codes.
3. Margin Differences Between Zip Codes (TotalPremium) Null Hypothesis (H₀): There is no significant margin (profit) difference between zip codes. Alternative Hypothesis (H₁): There is a significant margin (profit) difference between zip codes.
4. Risk Differences Between Men and Women (TotalClaims) Null Hypothesis (H₀): There is no significant risk difference between men and women. Alternative Hypothesis (H₁): There is a significant risk difference between men and women. 

## Steps in Task 3
1. Data Segmentation: For each hypothesis test, the dataset was segmented into two groups:
Control Group: Group A without a certain feature (e.g., province or gender). 
Test Group: Group B with a different feature (e.g., different province or gender). 
2. Statistical Testing: We used appropriate statistical tests based on the data type and feature.
T-test for continuous variables (TotalClaims, TotalPremium). 
Chi-square test for categorical variables (e.g., Gender vs. TotalClaims). 
3. Analysis and Reporting After performing the statistical tests, the p-values were compared to the significance level (alpha = 0.05) to either accept or reject the null hypothesis.

##Results

*Risk Differences Across Provinces (T-test) p-value: 0.0563 Conclusion: Fail to reject the null hypothesis (no significant result).
*Risk Differences Between Zip Codes (T-test) p-value: 0.5023 Conclusion: Fail to reject the null hypothesis (no significant result).
*Margin Differences Between Zip Codes (T-test) p-value: 1.48e-20 Conclusion: Reject the null hypothesis (significant result). This indicates significant margin differences between zip codes.
*Risk Differences Between Men and Women (Chi-square) p-value: 1.0 Conclusion: Fail to reject the null hypothesis (no significant result). 

##Insights and Recommendations 
*Location-Based Pricing: The significant margin differences between zip codes suggest that AlphaCare could adjust premiums based on location to optimize profitability.
*No Gender-Based Risk Adjustment: No significant risk difference was found between men and women. Thus, gender-based premium differentiation may not be necessary.
*Focus on Zip Code Segmentation: Further exploration of zip code-related risk and margin differences could lead to more refined marketing and pricing strategies.

#Task 4- Modeling

##Steps in Task 4

1. Data Preparation 
*Handling Missing Data: Imputed missing numerical values with the median and categorical values with the most frequent category. *Feature Engineering: Created new features where necessary, such as interaction terms or derived variables. 
*Encoding Categorical Variables: Converted categorical variables to a numerical format using one-hot encoding for model compatibility.
*Detecting outliers

2. Modeling Techniques
 We trained four models on the processed dataset:
*Linear Regression 
*Decision Tree Regressor 
*Random Forest Regressor 
*XGBoost Regressor 

3. Model Evaluation
 Each model was evaluated using:

*Mean Squared Error (MSE): Measures the average squared difference between actual and predicted values. 
*Mean Absolute Error (MAE): Measures the average absolute difference between actual and predicted values. 
*R-Squared: Indicates the proportion of variance explained by the model (closer to 1 is better). 

4. Feature Importance Analysis:
 SHAP (SHapley Additive exPlanations) was used to analyze feature importance for the Random Forest model, providing interpretability on how each feature contributed to the model’s predictions.

##Results

*Linear Regression Mean Squared Error: 4.62e+29 Mean Absolute Error: 1.94e+12 R-Squared: -9.45e+22 (Poor performance, likely due to data scaling issues or multicollinearity).
*Decision Tree Mean Squared Error: 761,858 Mean Absolute Error: 14.05 R-Squared: 0.844 (Strong performance with good predictive power).
*Random Forest Mean Squared Error: 1,491,559 Mean Absolute Error: 26.67 R-Squared: 0.821 (Good performance, slightly lower than Decision Tree).
*XGBoost Mean Squared Error: 1,311,496 Mean Absolute Error: 24.88 R-Squared: 0.835 (Comparable to Decision Tree and Random Forest). 

Feature Importance SHAP analysis indicated that features such as VehicleType, SumInsured, and CalculatedPremiumPerTerm had the most significant impact on the prediction of TotalClaims. Insights and Recommendations Decision Tree and XGBoost Models: Both models performed well in predicting TotalClaims with strong R-Squared values above 0.8. Decision Tree provided the best performance, but XGBoost showed competitive results, suggesting that both can be used effectively.

**Linear Regression Limitations: Linear Regression underperformed, possibly due to multicollinearity and outliers in the dataset. Further data transformation and scaling are necessary to improve performance for linear models.

**Focus on Important Features: Based on SHAP analysis, AlphaCare should focus on key features such as VehicleType, SumInsured, and CalculatedPremiumPerTerm when assessing risk and determining premiums.

**Model Choice for Future Use: AlphaCare should prioritize using Decision Tree and XGBoost for predictive analytics, as these models show strong predictive power and interpretability.