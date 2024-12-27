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

### 1. Data Loading

We start by loading the dataset into a Pandas DataFrame for analysis. The dataset was provided in a `.csv` file format.

import pandas as pd

Load the dataset
df = pd.read_csv("data/MachineLearningRating_v3.txt", delimiter="|") 
2. Data Summarization We use descriptive statistics to get an initial understanding of the dataset, including numerical features like TotalPremium, TotalClaims, and categorical variables such as Citizenship, LegalType, and VehicleType.

Data summary
print(df.describe(include='all')) 

3. Data Quality Assessment Missing Values: We check for missing values to assess data quality. Data Types: Review the data types of each column and ensure proper formatting (e.g., categorical variables, date columns). Outliers: Detect outliers using box plots, particularly for TotalPremium and TotalClaims.

Check for missing values
print(df.isnull().sum())

Check data types
print(df.dtypes) 

4. Univariate Analysis We explore the distribution of individual variables using:

Histograms for numerical columns like SumInsured, TotalPremium, and TotalClaims. Bar charts for categorical variables like Citizenship, VehicleType, and LegalType.

import matplotlib.pyplot as plt

Plot histogram for TotalPremium
df['TotalPremium'].hist(bins=50) plt.title('Distribution of TotalPremium') plt.xlabel('TotalPremium') plt.ylabel('Frequency') plt.show()

Plot bar chart for Citizenship
df['Citizenship'].value_counts().plot(kind='bar') plt.title('Citizenship Distribution') plt.xlabel('Citizenship') plt.ylabel('Count') plt.show() 

5. Bivariate and Multivariate Analysis We explore relationships between key variables, such as TotalPremium vs TotalClaims, using:

Scatter plots to visualize correlations. Correlation matrix to quantify the strength of relationships between numerical variables.

Scatter plot for TotalPremium vs TotalClaims
df.plot.scatter(x='TotalPremium', y='TotalClaims') plt.title('TotalPremium vs TotalClaims') plt.show()

Correlation matrix
correlation_matrix = df.corr() print(correlation_matrix) 

6. Outlier Detection We use box plots to detect outliers in numerical features, especially focusing on TotalPremium and TotalClaims.

Box plot for TotalPremium
df.boxplot(column='TotalPremium') plt.title('Box Plot for TotalPremium') plt.show() 

7. Data Visualization Three creative and meaningful visualizations were developed:

Distribution of TotalPremium. Citizenship Distribution. Correlation heatmap for numerical features. Key Findings Missing Values: Certain fields, like Citizenship and PostalCode, have missing values, which need to be addressed. Outliers: Significant outliers were detected in TotalPremium and TotalClaims. Correlations: There is a positive correlation between TotalPremium and TotalClaims, indicating that higher premiums are associated with more claims. Data Distribution: The distribution of TotalPremium is heavily skewed, suggesting the need for transformation or handling in future tasks.

Task 2: Data Version Control (DVC) Setup Objective The objective of Task 2 is to set up Data Version Control (DVC) for tracking data versions, enabling reproducibility of analysis, and ensuring proper management of data and model files.

Steps in Task 2 DVC Installation:

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