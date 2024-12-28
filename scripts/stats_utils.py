import pandas as pd
from scipy import stats
import numpy as np

def calculate_variability(data):
    """
    Calculate the variability (standard deviation) for numerical features.
    """
    return data[['TotalPremium', 'TotalClaims']].std()

from scipy import stats
import pandas as pd

def segment_data(df, feature, control_value, test_value):
    """
    Split data into control and test groups based on a feature value.
    
    :param df: DataFrame
    :param feature: Feature to split on (e.g., 'Province', 'PostalCode')
    :param control_value: Value for control group
    :param test_value: Value for test group
    :return: Control group, Test group DataFrames
    """
    control_group = df[df[feature] == control_value]
    test_group = df[df[feature] == test_value]
    return control_group, test_group

def perform_ttest(control_group, test_group, target_feature):
    """
    Conduct a T-test for two independent samples (control and test groups).
    
    :param control_group: DataFrame of the control group
    :param test_group: DataFrame of the test group
    :param target_feature: The feature for comparison (e.g., 'TotalClaims', 'TotalPremium')
    :return: p_value, t_statistic
    """
    if control_group.empty or test_group.empty:
        return None, None
    
    t_statistic, p_value = stats.ttest_ind(control_group[target_feature], test_group[target_feature], nan_policy='omit')
    return p_value, t_statistic

def perform_chi_square_test(df, feature1, feature2):
    """
    Perform a chi-square test for independence between two categorical features.
    
    :param df: DataFrame
    :param feature1: The first categorical feature (e.g., 'Gender')
    :param feature2: The second feature (e.g., 'TotalClaims')
    :return: p_value, chi2_statistic
    """
    contingency_table = pd.crosstab(df[feature1], df[feature2])
    chi2_statistic, p_value, _, _ = stats.chi2_contingency(contingency_table)
    return p_value, chi2_statistic

def report_hypothesis_result(p_value, alpha=0.05):
    """
    Interpret and report the result of the hypothesis test.
    
    :param p_value: P-value from statistical test
    :param alpha: Significance level (default is 0.05)
    :return: Conclusion string
    """
    if p_value is None:
        return "No valid data for testing."
    elif p_value < alpha:
        return "Reject the null hypothesis (significant result)."
    else:
        return "Fail to reject the null hypothesis (no significant result)."
