
# Product Demand Segments


import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(
    page_title="Product Demand Segments",
    layout="wide"
)

st.title("Product Demand Segmentation")


st.metric(
    "Number of Demand Clusters",
    "3"
)

st.markdown("---")

# Display Cluster Chart


st.subheader("Product Demand Clusters")

chart_path = "charts/product_clusters.png"

if os.path.exists(chart_path):

    image = Image.open(chart_path)

    st.image(
        image,
        use_container_width=True
    )

else:

    st.warning("Cluster chart not found.")


# Display Cluster Table


st.subheader("Sub-Category Cluster Assignment")

cluster_file = "clustering/product_clusters.csv"

if os.path.exists(cluster_file):

    cluster_df = pd.read_csv(cluster_file)

    display_df = cluster_df[
        [
            "Sub-Category",
            "Cluster"
        ]
    ].copy()

    # Meaningful Labels
    cluster_names = {
        0: "Premium / High Value Products",
        1: "Stable Everyday Demand",
        2: "High Volume & Growing Demand"
    }

    display_df["Cluster"] = display_df["Cluster"].map(cluster_names)

    st.dataframe(
        display_df,
        use_container_width=True
    )

else:

    st.warning("Cluster results not found.")


# Stocking Strategy


st.subheader("Recommended Stocking Strategy")

st.markdown("""

### Premium / High Value Products

Maintain safety stock and closely monitor inventory because stock shortages may result in significant revenue loss.

---

### Stable Everyday Demand

Maintain regular replenishment schedules with standard inventory levels to ensure consistent product availability.

---

### High Volume & Growing Demand

Prioritize inventory replenishment, maintain higher stock levels, and forecast demand frequently to prevent stock-outs during periods of increased customer demand.

""")