import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud

def generate_summary(df):
    summary = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.values,
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })
    return summary

def plot_distributions(df):
    figs = []
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_columns:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Distribution of {col}")
        figs.append(fig)
    return figs

def plot_correlation(df):
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if numeric_df.empty:
        return None
    fig, ax = plt.subplots()
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")
    return fig

def plot_missing_values(df):
    missing_data = df.isnull().sum()
    missing_data = missing_data[missing_data > 0]
    if missing_data.empty:
        return None
    fig, ax = plt.subplots()
    missing_data.plot(kind="bar", ax=ax, color="red")
    ax.set_title("Missing Values Count")
    return fig

def plot_time_series(df):
    time_cols = df.select_dtypes(include=["datetime64"]).columns
    figs = []
    for col in time_cols:
        fig, ax = plt.subplots()
        df[col].value_counts().sort_index().plot(ax=ax)
        ax.set_title(f"Time Series Plot for {col}")
        figs.append(fig)
    return figs

def plot_categorical(df):
    cat_cols = df.select_dtypes(include=["object"]).columns
    figs = []
    for col in cat_cols:
        fig, ax = plt.subplots()
        sns.countplot(y=df[col], ax=ax, order=df[col].value_counts().index)
        ax.set_title(f"Distribution of {col}")
        figs.append(fig)
    return figs

def plot_boxplot(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, ax=ax)
    return fig

def plot_wordcloud(text_column):
    text = ' '.join(text_column.dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    return fig
