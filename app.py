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
    heatmap_fig = plot_correlation(df)
    if heatmap_fig:
        st.pyplot(heatmap_fig)
    else:
        st.warning("No numeric columns available for correlation heatmap.")

    st.write("### 📈 Feature Distributions")
    fig = plot_distributions(df)

    st.plotly_chart(fig)

# Add About Me Section
st.sidebar.title("ℹ️ About This App")
st.sidebar.info(
    "This is an **Automated EDA & Insights App** that helps users quickly analyze datasets. "
    "It supports **advanced visualizations, missing values analysis, and dark/light mode customization.** "
    "Built with **Streamlit, Pandas, Matplotlib, and Plotly**."
)
st.sidebar.title("👨‍💻 About Me")
st.sidebar.info(
    "**Udit Katiyar**\n\n"
    "🚀 **Computer Science Engineer | Tech Enthusiast**\n\n"
    "💡 Passionate about **Web Development, AI/ML, and Open-Source Contributions**\n\n"
    "📝 Sharing thoughts on **cutting-edge technologies, problem-solving, and innovation**\n\n"
    "📚 Exploring **Cloud Computing, DevOps, and Blockchain**\n\n"
    "🔥 Always eager to learn and build amazing projects!"
)

st.sidebar.title("📢 Contact Me")
st.sidebar.info(
    "📧 **Email:** [uditkatiyar2005@gmail.com](mailto:uditkatiyar2005@gmail.com)\n"
    "🔗 **GitHub:** [github.com/katiyarudit](https://github.com/katiyarudit)\n"
    "💼 **LinkedIn:** [linkedin.com/in/udit1105](https://www.linkedin.com/in/udit1105/)(https://linkedin.com/in/udit-katiyar)\n"
    "📝 **Blog:** [Your Blog Link](https://yourblog.com)"
)
