import streamlit as st
import pandas as pd

from filters import apply_filters
from charts import (
    pie_chart,
    histogram_chart,
    line_chart,
    bar_chart,
    scatter_chart,
    box_chart,
    heatmap_chart,
    area_chart,
    count_chart,
    violin_chart
)

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Load Data
# ----------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/StudentsPerformance.csv")

    df["average_score"] = (
        df["math score"] +
        df["reading score"] +
        df["writing score"]
    ) / 3

    return df

df = load_data()

# ----------------------------
# Title
# ----------------------------

st.title("📊 Student Performance Dashboard")

st.markdown("""
Analyze student performance based on gender,
education, lunch type and test preparation.
""")

# ----------------------------
# Filters
# ----------------------------

filtered_df = apply_filters(df)

# ----------------------------
# KPI Cards
# ----------------------------

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric(
        "Total Students",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Avg Math",
        round(filtered_df["math score"].mean(),2)
    )

with col3:
    st.metric(
        "Avg Reading",
        round(filtered_df["reading score"].mean(),2)
    )

with col4:
    st.metric(
        "Avg Writing",
        round(filtered_df["writing score"].mean(),2)
    )

with col5:
    st.metric(
        "Highest Avg",
        round(filtered_df["average_score"].max(),2)
    )

st.divider()

# ----------------------------
# Charts Layout
# ----------------------------

c1,c2 = st.columns(2)

with c1:
    pie_chart(filtered_df)

with c2:
    histogram_chart(filtered_df)

c1,c2 = st.columns(2)

with c1:
    bar_chart(filtered_df)

with c2:
    line_chart(filtered_df)

c1,c2 = st.columns(2)

with c1:
    scatter_chart(filtered_df)

with c2:
    box_chart(filtered_df)

st.subheader("Correlation Heatmap")
heatmap_chart(filtered_df)

c1,c2 = st.columns(2)

with c1:
    area_chart(filtered_df)

with c2:
    count_chart(filtered_df)

st.subheader("Writing Score Distribution")
violin_chart(filtered_df)
