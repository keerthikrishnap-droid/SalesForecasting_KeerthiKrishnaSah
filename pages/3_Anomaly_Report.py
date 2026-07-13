
# Anomaly Report


import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(
    page_title="Anomaly Report",
    layout="wide"
)

st.title("Anomaly Report")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Isolation Forest",
        "11 anomalies"
    )

with col2:
    st.metric(
        "Z-Score",
        "6 anomalies"
    )

st.markdown("---")


# Display Isolation Forest Chart


st.subheader("Weekly Sales Anomalies")

image_path = "anomalies/isolation_forest.png"

if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, use_container_width=True)
else:
    st.warning("Isolation Forest chart not found.")


# Display Anomaly Table


st.subheader("Detected Anomalies")

csv_path = "anomalies/anomaly_comparison.csv"

if os.path.exists(csv_path):

    anomaly_df = pd.read_csv(csv_path)

    st.dataframe(
        anomaly_df[
        [
            "Week",
            "Weekly Sales",
            "Detected By"
        ]
    ],
        use_container_width=True
    )

else:
    st.warning("Anomaly comparison file not found.")