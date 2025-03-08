import streamlit as st
import pandas as pd
from eda import generate_summary, plot_distributions, plot_correlation, plot_missing_values

st.set_page_config(page_title="Dataset Insights & EDA", layout="wide", initial_sidebar_state="expanded")

st.title("📊 Automated EDA & Insights")

st.sidebar.title("⚙️ Settings")
theme = st.sidebar.radio("Select Theme", ["Light", "Dark"])
st.markdown(f'<style>body {{ background-color: {"#2E2E2E" if theme == "Dark" else "white"}; color: {"white" if theme == "Dark" else "black"} }}</style>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📂 Upload a Dataset (CSV format)", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 📌 Dataset Preview")
    st.dataframe(df.head())

    st.write("### 📊 Dataset Summary")
    st.dataframe(generate_summary(df))

    st.write("### 🔍 Missing Values")
    st.pyplot(plot_missing_values(df))

    st.write("### 🔄 Correlation Heatmap")
    st.pyplot(plot_correlation(df))

    st.write("### 📈 Feature Distributions")
    for fig in plot_distributions(df):
        st.plotly_chart(fig)
