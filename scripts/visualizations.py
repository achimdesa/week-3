import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    """Function to plot histogram for a numerical column."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Histogram of {column}")
    plt.show()

def plot_bar_chart(df, column):
    """Function to plot bar chart for a categorical column."""
    plt.figure(figsize=(8, 5))
    df[column].value_counts().plot(kind='bar')
    plt.title(f"Bar Chart of {column}")
    plt.show()

def plot_correlation_matrix(df, columns):
    """Function to plot correlation matrix."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[columns].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def plot_scatter(df, x_col, y_col):
    """Function to plot scatter plot for bivariate analysis."""
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x=x_col, y=y_col)
    plt.title(f"Scatter Plot of {x_col} vs {y_col}")
    plt.show()
