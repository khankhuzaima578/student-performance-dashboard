# Student Performance Analysis Dashboard

## Project Overview

This project is an interactive data visualization dashboard developed using Python and Streamlit. The dashboard analyzes the Students Performance in Exams dataset and provides meaningful insights into student academic performance based on demographic and educational factors.

The dashboard includes data cleaning, preprocessing, interactive filters, KPI cards, and multiple visualizations to help users explore relationships between different variables and student scores.

---

## Dataset

Dataset Name: Students Performance in Exams

Features:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch
* Test Preparation Course
* Math Score
* Reading Score
* Writing Score

---

## Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

---

## Dashboard Features

### KPI Cards

* Total Students
* Average Math Score
* Average Reading Score
* Average Writing Score
* Highest Average Score

### Interactive Filters

* Gender Filter
* Race/Ethnicity Filter
* Test Preparation Filter
* Math Score Range Slider
* Reset Filters Button

### Visualizations

1. Pie Chart – Gender Distribution
2. Histogram – Math Score Distribution
3. Bar Chart – Average Math Score by Gender
4. Line Chart – Average Scores by Parent Education
5. Scatter Plot – Reading Score vs Writing Score
6. Box Plot – Math Score by Gender
7. Heatmap – Correlation Analysis
8. Area Chart – Average Score Trends
9. Count Plot – Race/Ethnicity Distribution
10. Violin Plot – Writing Score by Test Preparation

---

## Project Structure

dashboard_project/

data/

* StudentsPerformance.csv

app.py

charts.py

filters.py

requirements.txt

README.md

---

## Installation

Install required packages:

pip install -r requirements.txt

---

## Running the Dashboard

Run the following command:

streamlit run app.py

The dashboard will open in your browser automatically.

---

## Key Insights

* Female students generally perform better in reading and writing.
* Students who complete test preparation courses tend to achieve higher scores.
* Reading and writing scores show a strong positive correlation.
* Parental education level has a noticeable impact on student performance.
* Lunch type and preparation courses influence academic outcomes.

---

## Course

Exploratory Data Analysis (EDA)

## Instructor

Ali Hassan Sherazi

## Student

Muhammad Khuzaima

---

## Conclusion

This dashboard provides an interactive and user-friendly platform for analyzing student performance data. Through visual analytics and filtering capabilities, users can identify trends, compare groups, and gain valuable educational insights.
