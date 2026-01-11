import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Simple Sales Dashboard",
                   layout="wide")

# Dummy Data
@st.cache_data
def load_data():
    np.random.seed(42)
    data = {
        "Date": pd.date_range("2024-01-01", periods=60),
        "Region": ["North", "South", "East", "West"] * 15,
        "Product": ["Chai", "Coffee", "Green Tea"] * 20,
        "Revenue": np.random.randint(20, 100, 60)
    }
    return pd.DataFrame(data)

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
region_filter = st.sidebar.multiselect("Select Region", df
["Region"].unique(), default=df["Region"].unique())
product_filter = st.sidebar.multiselect("Select Product", df
["Product"].unique(), default=df["Product"].unique())

# Filter Data
filtered_df = df[df["Region"].isin(region_filter) & df
["Product"].isin(product_filter)]

# KPI Section
st.title("Simple Sales Dasboard")
st.write("Columns:", filtered_df.columns)
st.write(filtered_df.head())
total_revenue = filtered_df["Revenue"].sum()
st.write("ACTUAL Columns:", filtered_df.columns.tolist())
st.write(filtered_df.head())

def load_data():
    df = pd.Dataframe({
        "Date": pd.date_range("2024-01-01", periods=60),
        "Sales": np.random.randint(1000, 5000, 60),
        "Units Sold": np.random.randint(10, 100, 60)
    })