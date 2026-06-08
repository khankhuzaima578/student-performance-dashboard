import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Professional Style
sns.set_style("whitegrid")


# ---------------------------------------------------
# PIE CHART
# ---------------------------------------------------

def pie_chart(df):

    st.subheader("Gender Distribution")

    fig, ax = plt.subplots(figsize=(6, 5))

    df["gender"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        ax=ax
    )

    ax.set_ylabel("")

    st.pyplot(fig)


# ---------------------------------------------------
# HISTOGRAM
# ---------------------------------------------------

def histogram_chart(df):

    st.subheader("Math Score Distribution")

    fig, ax = plt.subplots(figsize=(6, 5))

    sns.histplot(
        df["math score"],
        bins=15,
        kde=True,
        ax=ax
    )

    ax.set_xlabel("Math Score")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)


# ---------------------------------------------------
# BAR CHART
# ---------------------------------------------------

def bar_chart(df):

    st.subheader("Average Math Score by Gender")

    fig, ax = plt.subplots(figsize=(6, 5))

    sns.barplot(
        data=df,
        x="gender",
        y="math score",
        ax=ax
    )

    ax.set_xlabel("Gender")
    ax.set_ylabel("Average Math Score")

    st.pyplot(fig)


# ---------------------------------------------------
# LINE CHART
# ---------------------------------------------------

def line_chart(df):

    st.subheader("Average Scores by Parent Education")

    education = df.groupby(
        "parental level of education"
    )[
        [
            "math score",
            "reading score",
            "writing score"
        ]
    ].mean()

    fig, ax = plt.subplots(figsize=(8, 5))

    education.plot(
        marker="o",
        ax=ax
    )

    ax.set_ylabel("Average Score")

    st.pyplot(fig)


# ---------------------------------------------------
# SCATTER PLOT
# ---------------------------------------------------

def scatter_chart(df):

    st.subheader("Reading Score vs Writing Score")

    fig, ax = plt.subplots(figsize=(6, 5))

    sns.scatterplot(
        data=df,
        x="reading score",
        y="writing score",
        hue="gender",
        ax=ax
    )

    st.pyplot(fig)


# ---------------------------------------------------
# BOX PLOT
# ---------------------------------------------------

def box_chart(df):

    st.subheader("Math Score by Gender")

    fig, ax = plt.subplots(figsize=(6, 5))

    sns.boxplot(
        data=df,
        x="gender",
        y="math score",
        ax=ax
    )

    st.pyplot(fig)


# ---------------------------------------------------
# HEATMAP
# ---------------------------------------------------

def heatmap_chart(df):

    corr = df[
        [
            "math score",
            "reading score",
            "writing score",
            "average_score"
        ]
    ].corr()

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax
    )

    st.pyplot(fig)


# ---------------------------------------------------
# AREA CHART
# ---------------------------------------------------

def area_chart(df):

    st.subheader("Average Score Trends")

    area = df.groupby(
        "parental level of education"
    )[
        [
            "math score",
            "reading score",
            "writing score"
        ]
    ].mean()

    fig, ax = plt.subplots(figsize=(8, 5))

    area.plot.area(
        alpha=0.6,
        ax=ax
    )

    ax.set_ylabel("Average Score")

    st.pyplot(fig)


# ---------------------------------------------------
# COUNT PLOT
# ---------------------------------------------------

def count_chart(df):

    st.subheader("Race/Ethnicity Distribution")

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="race/ethnicity",
        ax=ax
    )

    ax.set_xlabel("Race/Ethnicity")
    ax.set_ylabel("Count")

    st.pyplot(fig)


# ---------------------------------------------------
# VIOLIN PLOT
# ---------------------------------------------------

def violin_chart(df):

    st.subheader("Writing Score by Test Preparation")

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.violinplot(
        data=df,
        x="test preparation course",
        y="writing score",
        ax=ax
    )

    st.pyplot(fig)
