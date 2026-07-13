# ==========================================================
# Sales Overview Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Sales Overview",
    layout="wide"
)

st.title("Sales Overview Dashboard")

st.write(
    "Explore yearly, monthly, regional, and category-wise sales performance."
)

st.markdown("---")

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("train.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="%d/%m/%Y"
    )

    return df


df = load_data()

# ----------------------------------------------------------
# Sidebar Filters
# ----------------------------------------------------------

st.sidebar.title("Filters")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["Region"].unique())
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category"].unique())
)

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

# ----------------------------------------------------------
# Summary Cards
# ----------------------------------------------------------

total_sales = filtered_df["Sales"].sum()
total_orders = filtered_df["Order ID"].nunique()
average_order = filtered_df["Sales"].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sales",
        f"${total_sales:,.2f}"
    )

with col2:
    st.metric(
        "Total Orders",
        f"{total_orders:,}"
    )

with col3:
    st.metric(
        "Average Order Value",
        f"${average_order:,.2f}"
    )

st.markdown("---")

# ----------------------------------------------------------
# Yearly Sales
# ----------------------------------------------------------

yearly_sales = (
    filtered_df
    .groupby(filtered_df["Order Date"].dt.year)["Sales"]
    .sum()
)

fig_year, ax = plt.subplots(figsize=(6,4))

ax.bar(
    yearly_sales.index.astype(str),
    yearly_sales.values
)

ax.set_title("Total Sales by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Sales")

# ----------------------------------------------------------
# Monthly Sales
# ----------------------------------------------------------

monthly_sales = (
    filtered_df
    .groupby(
        pd.Grouper(
            key="Order Date",
            freq="ME"
        )
    )["Sales"]
    .sum()
)

fig_month, ax = plt.subplots(figsize=(6,4))

ax.plot(
    monthly_sales.index,
    monthly_sales.values,
    linewidth=2
)

ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

# ----------------------------------------------------------
# Display Charts
# ----------------------------------------------------------

left, right = st.columns(2)

with left:
    st.pyplot(fig_year)
    plt.close(fig_year)

with right:
    st.pyplot(fig_month)
    plt.close(fig_month)

st.markdown("---")

# ==========================================================
# Sales by Region
# ==========================================================

st.subheader("Sales by Region")

region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(
    region_sales["Region"],
    region_sales["Sales"]
)

ax.set_title("Sales by Region")
ax.set_xlabel("Region")
ax.set_ylabel("Sales")

st.pyplot(fig)
plt.close(fig)

st.write("Region-wise Sales Summary")

st.dataframe(
    region_sales,
    width="stretch"
)

st.markdown("---")

# ==========================================================
# Sales by Category
# ==========================================================

st.subheader("Sales by Category")

category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(
    category_sales["Category"],
    category_sales["Sales"]
)

ax.set_title("Sales by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Sales")

plt.xticks(rotation=20)

st.pyplot(fig)
plt.close(fig)

st.write("Category-wise Sales Summary")

st.dataframe(
    category_sales,
    width="stretch"
)
