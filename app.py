
# Sales Forecasting Dashboard


import streamlit as st

st.set_page_config(
    page_title="Retail Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Retail Sales Forecasting Dashboard")

st.markdown("---")

st.markdown("""
## Welcome

This dashboard was developed as part of a Sales Forecasting and Demand Analysis project.

The application provides:

- 📊 Sales Overview Dashboard
- 🔮 Sales Forecast Explorer
- 🚨 Sales Anomaly Detection
- 📦 Product Demand Segmentation

Use the navigation panel on the left to explore each module.
""")

st.markdown("---")

st.subheader("Project Workflow")

st.markdown("""
1. Data Cleaning & Aggregation
2. Exploratory Data Analysis
3. Time Series Forecasting
4. Product & Region Forecasting
5. Anomaly Detection
6. Product Demand Segmentation
7. Interactive Dashboard
""")

st.success("Select a page from the sidebar to begin.")