
# Forecast Explorer


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet




st.set_page_config(
    page_title="Forecast Explorer",
    layout="wide"
)

st.title("Forecast Explorer")


# Load Dataset


@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="%d/%m/%Y"
    )

    return df

df = load_data()


# User Inputs


forecast_type = st.selectbox(
    "Forecast Type",
    ["Category", "Region"]
)

if forecast_type == "Category":
    selected = st.selectbox(
        "Select Category",
        sorted(df["Category"].unique())
    )

    filtered_df = df[df["Category"] == selected]

else:
    selected = st.selectbox(
        "Select Region",
        sorted(df["Region"].unique())
    )

    filtered_df = df[df["Region"] == selected]

forecast_horizon = st.slider(
    "Forecast Horizon (Months)",
    min_value=1,
    max_value=3,
    value=3
)


# Prepare Monthly Sales


monthly = (
    filtered_df
    .groupby(
        pd.Grouper(
            key="Order Date",
            freq="ME"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

monthly.columns = ["ds", "y"]


# Train Prophet


model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)

model.fit(monthly)

future = model.make_future_dataframe(
    periods=forecast_horizon,
    freq="ME"
)

forecast = model.predict(future)


# Plot Forecast


st.subheader("Forecast")

fig = model.plot(forecast)

st.pyplot(fig)


# Forecast Table


st.subheader("Forecast Values")

future_values = forecast.tail(forecast_horizon)[
    [
        "ds",
        "yhat",
        "yhat_lower",
        "yhat_upper"
    ]
]

future_values.columns = [
    "Month",
    "Forecast",
    "Lower CI",
    "Upper CI"
]

st.dataframe(future_values)


# Model Performance


st.subheader("Model Performance")

# st.write("Model Used: Prophet")

# st.write("MAE : 14309.99")

# st.write("RMSE : 18954.58")
metrics = pd.read_csv(
    "forecasts/forecast_metrics.csv"
)

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric(
        "Model",
        metrics.loc[0, "Model"]
    )

with metric2:
    st.metric(
        "MAE",
        f"{metrics.loc[0, 'MAE']:,.2f}"
    )

with metric3:
    st.metric(
        "RMSE",
        f"{metrics.loc[0, 'RMSE']:,.2f}"
    )

# col1, col2 = st.columns(2)

# with col1:
#     st.metric("MAE", "14,309.99")

# with col2:
#     st.metric("RMSE", "18,954.58")