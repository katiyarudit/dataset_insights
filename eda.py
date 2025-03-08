import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import missingno as msno

def generate_summary(df):
    summary = pd.DataFrame({
        'Column': df.columns,
        'Non-null Count': df.count(),
        'Unique Values': df.nunique(),
        'Data Type': df.dtypes
    })
    return summary

def plot_distributions(df):
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        fig = px.histogram(df, x=col, title=f'Distribution of {col}')
        yield fig

def plot_correlation(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    return fig

def plot_missing_values(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    msno.bar(df, ax=ax)
    return fig
