import pandas as pd
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
def load_data(file_path):
    """Function to load data from a CSV file."""
    try:
        df = pd.read_csv(file_path, delimiter='|', low_memory=False)  
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """
    Clean the data by removing rows with missing or zero values in critical columns
    such as TotalPremium and TotalClaims.
    """
    # Remove rows with missing or zero values for key metrics
    df_clean = df.dropna(subset=['TotalPremium', 'TotalClaims'])
    df_clean = df_clean[df_clean['TotalPremium'] != 0]
    df_clean = df_clean[df_clean['TotalClaims'] != 0]
    
    return df_clean
def load_data2(file_path):
    """Function to load data from a CSV file."""
    try:
        # Load the data with appropriate data types
        df = pd.read_csv(file_path, delimiter='|', low_memory=False,
                         dtype={'TotalClaims': 'float64', 'TotalPremium': 'float64'},
                         na_values=['', ' ', 'NaN'])  # Handle missing values
        
        # Handle non-numeric or mixed-type columns by forcing them to numeric
        df['TotalClaims'] = pd.to_numeric(df['TotalClaims'], errors='coerce')
        df['TotalPremium'] = pd.to_numeric(df['TotalPremium'], errors='coerce')
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
def summarize_data(df):
    """Function to summarize the dataframe."""
    return df.describe(include='all')

def check_missing_values(df):
    """Function to check for missing values."""
    return df.isnull().sum()

def check_data_types(df):
    """Function to check data types of each column."""
    return df.dtypes

def detect_outliers(df, column):
    """Function to detect outliers using the IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return df[((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))]


def handle_missing_data(df):
    # Handle missing numerical values
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # Remove any columns that are entirely missing or have invalid data
    df_numerical = df[numerical_columns].dropna(axis=1, how='all')

    # Use SimpleImputer to fill missing values for numerical columns
    imputer = SimpleImputer(strategy='median')
    numerical_data = imputer.fit_transform(df_numerical)
    
    # Ensure that the transformed data is returned as a DataFrame
    df_numerical_imputed = pd.DataFrame(numerical_data, columns=df_numerical.columns, index=df.index)

    # Handle missing categorical values
    categorical_columns = df.select_dtypes(include=['object']).columns
    df_categorical = df[categorical_columns].dropna(axis=1, how='all')
    
    imputer_cat = SimpleImputer(strategy='most_frequent')
    categorical_data = imputer_cat.fit_transform(df_categorical)
    
    # Convert the categorical data back to a DataFrame
    df_categorical_imputed = pd.DataFrame(categorical_data, columns=df_categorical.columns, index=df.index)
    
    # Combine both numerical and categorical columns into a single DataFrame
    df_cleaned = pd.concat([df_numerical_imputed, df_categorical_imputed], axis=1)
    
    return df_cleaned

def encode_categorical_data(df):
    df_encoded = pd.get_dummies(df, drop_first=True)  # One-hot encoding
    return df_encoded

def feature_engineering(df):
    # Example: create a new feature if necessary
    df['Premium_to_Claim_Ratio'] = df['TotalPremium'] / (df['TotalClaims'] + 1)
    return df