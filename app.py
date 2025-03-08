import streamlit as st
import pandas as pd
from eda_functions import (
    generate_summary, plot_distributions, plot_correlation, plot_missing_values,
    plot_time_series, plot_categorical, plot_boxplot, plot_wordcloud
)

st.set_page_config(page_title="Dataset Insights & EDA", layout="wide")

st.title("📊 Automated EDA & Insights")
st.markdown("Welcome to the Automated EDA Tool! Upload a dataset and explore insights effortlessly.")

st.sidebar.title("⚙️ Settings")
theme = st.sidebar.radio("Select Theme", ["Light", "Dark"])
st.markdown(f'<style>body {{ background-color: {"#2E2E2E" if theme == "Dark" else "white"}; color: {"white" if theme == "Dark" else "black"} }}</style>', unsafe_allow_html=True)

st.sidebar.title("📌 About This App")
st.sidebar.info("This tool helps users explore datasets by generating automatic visualizations and summaries.")

st.sidebar.title("🧑‍💻 About Me")
st.sidebar.info("""
👋 **Hello, I'm Udit Katiyar!**  
- 🎓 Computer Science Engineering Student at LPU  
- 📍 From Kanpur  
- 🚀 Passionate about Machine Learning & Web Development  
- 🛠️ Working on real-time data visualization projects  
- 🔗 Connect with me on [GitHub](https://github.com/) or [LinkedIn](https://linkedin.com/)
""")

data_type = st.sidebar.selectbox("Select Data Type", [
    "Numerical Data (Continuous)", "Categorical Data (Discrete)", "Time-Series Data",
    "Correlation Data", "Missing Values Data", "Text Data (NLP)"
])

data_examples = {
    "Numerical Data (Continuous)": "Examples: Age, Salary, Temperature",
    "Categorical Data (Discrete)": "Examples: Gender, Country, Product Type",
    "Time-Series Data": "Examples: Stock Prices, Sales Over Time",
    "Correlation Data": "Examples: Health Factors vs. Disease",
    "Missing Values Data": "Examples: Incomplete Survey Responses",
    "Text Data (NLP)": "Examples: Customer Reviews, Social Media Comments"
}

st.sidebar.info(data_examples[data_type])

uploaded_file = st.file_uploader("📂 Upload a Dataset (CSV format)", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 📌 Dataset Preview")
else:
    st.write("### 📌 Dataset Preview (Default: Iris Dataset)")
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

st.dataframe(df.head())

st.write("### 📊 Dataset Summary")
st.dataframe(generate_summary(df))

if data_type == "Numerical Data (Continuous)":
    st.write("### 📈 Feature Distributions")
    for fig in plot_distributions(df):
        st.pyplot(fig)
    st.write("### 📦 Box Plot")
    st.pyplot(plot_boxplot(df))

elif data_type == "Categorical Data (Discrete)":
    st.write("### 📊 Category Distribution")
    for fig in plot_categorical(df):
        st.pyplot(fig)

elif data_type == "Time-Series Data":
    st.write("### 📈 Time Series Analysis")
    for fig in plot_time_series(df):
        st.pyplot(fig)

elif data_type == "Correlation Data":
    st.write("### 🔄 Correlation Heatmap")
    heatmap_fig = plot_correlation(df)
    if heatmap_fig:
        st.pyplot(heatmap_fig)

elif data_type == "Missing Values Data":
    st.write("### 🔍 Missing Values")
    missing_fig = plot_missing_values(df)
    if missing_fig:
        st.pyplot(missing_fig)

elif data_type == "Text Data (NLP)":
    text_column = st.selectbox("Select a Text Column", df.columns)
    st.write("### ☁️ Word Cloud")
    st.pyplot(plot_wordcloud(df[text_column]))
