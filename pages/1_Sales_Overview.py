

st.subheader("Sales by Region")

region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

st.dataframe(region_sales)


# # Sales Overview Dashboard


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt


# # Page Configuration


# st.set_page_config(
#     page_title="Sales Overview",
#     layout="wide"
# )

# st.title("Sales Overview Dashboard")

# st.write(
#     "Explore yearly, monthly, regional, and category-wise sales performance."
# )

# st.markdown("---")


# # Load Dataset


# @st.cache_data
# def load_data():
#     df = pd.read_csv("train.csv")

#     df["Order Date"] = pd.to_datetime(
#         df["Order Date"],
#         format="%d/%m/%Y"
#     )

#     return df

# df = load_data()


# # Sidebar Filters


# st.sidebar.title("Filters")

# selected_region = st.sidebar.selectbox(
#     "Select Region",
#     ["All"] + sorted(df["Region"].unique())
# )

# selected_category = st.sidebar.selectbox(
#     "Select Category",
#     ["All"] + sorted(df["Category"].unique())
# )

# filtered_df = df.copy()

# if selected_region != "All":
#     filtered_df = filtered_df[
#         filtered_df["Region"] == selected_region
#     ]

# if selected_category != "All":
#     filtered_df = filtered_df[
#         filtered_df["Category"] == selected_category
#     ]


# # Summary Cards


# total_sales = filtered_df["Sales"].sum()
# total_orders = filtered_df["Order ID"].nunique()
# average_order = filtered_df["Sales"].mean()

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric(
#         "Total Sales",
#         f"${total_sales:,.2f}"
#     )

# with col2:
#     st.metric(
#         "Total Orders",
#         f"{total_orders:,}"
#     )

# with col3:
#     st.metric(
#         "Average Order Value",
#         f"${average_order:,.2f}"
#     )

# st.markdown("---")


# # Yearly Sales


# yearly_sales = (
#     filtered_df
#     .groupby(filtered_df["Order Date"].dt.year)["Sales"]
#     .sum()
# )

# fig_year, ax = plt.subplots(figsize=(6,4))

# ax.bar(
#     yearly_sales.index.astype(str),
#     yearly_sales.values
# )

# ax.set_title("Total Sales by Year")
# ax.set_xlabel("Year")
# ax.set_ylabel("Sales")


# # Monthly Sales


# monthly_sales = (
#     filtered_df
#     .groupby(
#         pd.Grouper(
#             key="Order Date",
#             freq="ME"
#         )
#     )["Sales"]
#     .sum()
# )

# fig_month, ax = plt.subplots(figsize=(6,4))

# ax.plot(
#     monthly_sales.index,
#     monthly_sales.values,
#     linewidth=2
# )

# ax.set_title("Monthly Sales Trend")
# ax.set_xlabel("Month")
# ax.set_ylabel("Sales")


# # Display Charts Side by Side


# left, right = st.columns(2)

# with left:
#     st.pyplot(fig_year)

# with right:
#     st.pyplot(fig_month)

# st.markdown("---")


# # Sales by Region


# with st.expander("Sales by Region", expanded=True):

#     region_sales = (
#         filtered_df
#         .groupby("Region")["Sales"]
#         .sum()
#         .reset_index()
#     )

#     region_view = st.radio(
#         "View",
#         ["Bar Chart", "Table"],
#         horizontal=True,
#         key="region"
#     )

#     if region_view == "Bar Chart":

#         fig, ax = plt.subplots(figsize=(6,4))

#         ax.bar(
#             region_sales["Region"],
#             region_sales["Sales"]
#         )

#         ax.set_title("Sales by Region")

#         st.pyplot(fig)

#     else:

#         st.dataframe(
#             region_sales,
#             use_container_width=True
#         )


# # Sales by Category


# with st.expander("Sales by Category", expanded=True):

#     category_sales = (
#         filtered_df
#         .groupby("Category")["Sales"]
#         .sum()
#         .reset_index()
#     )

#     category_view = st.radio(
#         "View",
#         ["Bar Chart", "Table"],
#         horizontal=True,
#         key="category"
#     )

#     if category_view == "Bar Chart":

#         fig, ax = plt.subplots(figsize=(6,4))

#         ax.bar(
#             category_sales["Category"],
#             category_sales["Sales"]
#         )

#         ax.set_title("Sales by Category")

#         plt.xticks(rotation=20)

#         st.pyplot(fig)

#     else:

#         st.dataframe(
#             category_sales,
#             use_container_width=True
#         )

# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # st.set_page_config(
# #     page_title="Sales Overview",
# #     layout="wide"
# # )

# # st.title("Sales Overview Dashboard")


# # # Load Dataset


# # @st.cache_data
# # def load_data():
# #     df = pd.read_csv("train.csv")
# #     df["Order Date"] = pd.to_datetime(df["Order Date"],format="%d/%m/%Y")
# #     return df

# # df = load_data()


# # # Sidebar Filters


# # st.sidebar.header("Filters")

# # selected_region = st.sidebar.selectbox(
# #     "Select Region",
# #     ["All"] + sorted(df["Region"].unique().tolist())
# # )

# # selected_category = st.sidebar.selectbox(
# #     "Select Category",
# #     ["All"] + sorted(df["Category"].unique().tolist())
# # )

# # filtered_df = df.copy()

# # if selected_region != "All":
# #     filtered_df = filtered_df[
# #         filtered_df["Region"] == selected_region
# #     ]

# # if selected_category != "All":
# #     filtered_df = filtered_df[
# #         filtered_df["Category"] == selected_category
# #     ]


# # #

# # # Summary Statistics


# # total_sales = filtered_df["Sales"].sum()
# # total_orders = filtered_df["Order ID"].nunique()
# # average_order = filtered_df["Sales"].mean()

# # col1, col2, col3 = st.columns(3)

# # with col1:
# #     st.metric(
# #         "Total Sales",
# #         f"${total_sales:,.2f}"
# #     )

# # with col2:
# #     st.metric(
# #         "Total Orders",
# #         f"{total_orders:,}"
# #     )

# # with col3:
# #     st.metric(
# #         "Average Order Value",
# #         f"${average_order:,.2f}"
# #     )

# # st.markdown("---")

# # #

# # # Total Sales by Year


# # st.subheader("Total Sales by Year")

# # yearly_sales = (
# #     filtered_df
# #     .groupby(filtered_df["Order Date"].dt.year)["Sales"]
# #     .sum()
# # )

# # fig, ax = plt.subplots(figsize=(8,5))

# # ax.bar(
# #     yearly_sales.index.astype(str),
# #     yearly_sales.values
# # )

# # ax.set_xlabel("Year")
# # ax.set_ylabel("Sales")
# # ax.set_title("Yearly Sales")

# # st.pyplot(fig)


# # # Monthly Sales Trend


# # st.subheader("Monthly Sales Trend")

# # monthly_sales = (
# #     filtered_df
# #     .groupby(
# #         pd.Grouper(
# #             key="Order Date",
# #             freq="ME"
# #         )
# #     )["Sales"]
# #     .sum()
# # )

# # fig, ax = plt.subplots(figsize=(10,5))

# # ax.plot(
# #     monthly_sales.index,
# #     monthly_sales.values,
# #     linewidth=2
# # )

# # ax.set_xlabel("Month")
# # ax.set_ylabel("Sales")
# # ax.set_title("Monthly Sales Trend")

# # st.pyplot(fig)


# # # Sales by Region


# # st.subheader("Sales by Region")

# # region_sales = (
# #     filtered_df
# #     .groupby("Region")["Sales"]
# #     .sum()
# # )

# # st.dataframe(region_sales.reset_index())


# # # Sales by Category


# # st.subheader("Sales by Category")

# # category_sales = (
# #     filtered_df
# #     .groupby("Category")["Sales"]
# #     .sum()
# # )

# # st.dataframe(category_sales.reset_index())
