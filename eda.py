import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def generate_summary(df):
    numeric_df = df.select_dtypes(include=['number'])
    summary = {
        "Number of Rows": df.shape[0],
        "Number of Columns": df.shape[1],
        "Missing Values": df.isnull().sum().to_dict(),
        "Column Data Types": df.dtypes.to_dict(),
        "Mean": numeric_df.mean().to_dict(),
        "Median": numeric_df.median().to_dict(),
        "Standard Deviation": numeric_df.std().to_dict(),
        "Min Values": numeric_df.min().to_dict(),
        "Max Values": numeric_df.max().to_dict(),
        "25th Percentile": numeric_df.quantile(0.25).to_dict(),
        "50th Percentile (Median)": numeric_df.quantile(0.50).to_dict(),
        "75th Percentile": numeric_df.quantile(0.75).to_dict(),
    }
    return summary

def plot_distributions(df):
    numeric_df = df.select_dtypes(include=['number'])
    if numeric_df.empty:
        st.write("No numeric columns available for distribution plots.")
        return None
    fig, ax = plt.subplots(figsize=(12, 8))
    numeric_df.hist(ax=ax, bins=30)
    plt.suptitle("Feature Distributions")
    st.pyplot(fig)
    return fig

def plot_missing_values(df):
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    if missing_values.empty:
        st.write("No missing values in the dataset.")
        return None
    fig, ax = plt.subplots(figsize=(10, 5))
    missing_values.plot(kind='bar', ax=ax)
    ax.set_title("Missing Values per Column")
    ax.set_xlabel("Columns")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    return fig

def plot_correlation(df):
    df = df.apply(pd.to_numeric, errors='coerce')
    numeric_df = df.select_dtypes(include=['number'])
    if numeric_df.empty:
        st.write("No numeric columns available for correlation heatmap.")
        return None
    corr_matrix = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title("Feature Correlation Heatmap")
    st.pyplot(fig)
    return fig

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    dataset_path = "skoda.csv"
    df = load_dataset(dataset_path)
    df = df.apply(pd.to_numeric, errors='coerce')
    
    st.write("### Dataset Summary")
    st.write(generate_summary(df))
    
    st.write("### Feature Distributions")
    fig = plot_distributions(df)
    if fig:
        st.pyplot(fig)
    
    st.write("### Missing Values")
    fig = plot_missing_values(df)
    if fig:
        st.pyplot(fig)
    
    st.write("### Correlation Heatmap")
    fig = plot_correlation(df)
    if fig:
        st.pyplot(fig)
