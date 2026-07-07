# Customer Segmentation Using Clustering

A web-based Customer Segmentation System built using **Django**, **Machine Learning (K-Means Clustering)**, **Pandas**, **Scikit-learn**, and **Plotly**. The application helps businesses analyze customer behavior, segment customers into meaningful groups, and generate interactive visual reports.

---

## 📌 Project Overview

Customer segmentation is an important marketing strategy that divides customers into groups based on purchasing behavior, annual income, age, and spending score.

This project allows users to:

- Upload customer datasets
- Analyze customer data
- Perform K-Means clustering
- Visualize customer segments
- Export reports in CSV, Excel, and PDF formats

---

# ✨ Features

## Authentication

- User Registration
- User Login
- Logout
- Session Management

---

## Dashboard

- Welcome Dashboard
- Total Customers
- Average Income
- Average Spending Score
- Gender Statistics
- Dataset Health
- Interactive Charts

---

## Customers Module

- Customer List
- Search Customers
- Customer Statistics
- Membership Levels
- Customer Status
- Customer Details
- Responsive Table

---

## Analytics Module

- Age Distribution
- Gender Distribution
- Income Distribution
- Spending Score Distribution
- Scatter Plot
- Customer Segment Statistics

---

## Clustering Module

- K-Means Clustering
- Customer Segmentation
- Segment Summary
- Interactive Cluster Visualization

---

## Elbow Method

- Automatic Cluster Evaluation
- WCSS Calculation
- Optimal Cluster Selection
- Elbow Curve Visualization

---

## Dataset Upload

- Upload CSV File
- Automatic Data Validation
- Automatic Data Cleaning
- Real-Time Analysis

---

## Reports

- Export CSV
- Export Excel
- Export PDF
- Dataset Summary

---

## Settings

- User Profile
- Dataset Information
- Application Information

---

# 🛠 Technologies Used

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Font Awesome

---

## Backend

- Django
- Python

---

## Machine Learning

- Scikit-learn
- K-Means Clustering

---

## Data Analysis

- Pandas
- NumPy

---

## Visualization

- Plotly

---

## Database

- SQLite

---

# 📂 Project Structure

```
Customer-Segmentation-Using-Clustering/

│
├── accounts/
│
├── clustering/
│
├── config/
│
├── customers/
│
├── dashboard/
│
├── dataset/
│     └── Mall_Customers.csv
│
├── media/
│
├── reports/
│
├── static/
│     ├── css/
│     ├── js/
│     └── images/
│
├── templates/
│     └── pages/
│
├── db.sqlite3
│
├── manage.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Installation

## Step 1

Clone the repository

```bash
git clone https://github.com/giridharkalapala/CustomerSegmentationUsingClustering.git
```

---

## Step 2

Open the project

```bash
cd CustomerSegmentationUsingClustering
```

---

## Step 3

Create Virtual Environment

Windows

```bash
python -m venv venv
```

Linux

```bash
python3 -m venv venv
```

---

## Step 4

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

## Step 5

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6

Run Migrations

```bash
python manage.py migrate
```

---

## Step 7

Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

## Step 8

Run Server

```bash
python manage.py runserver
```

---

Open Browser

```
http://127.0.0.1:8000
```

---

# 📊 Dataset Format

The uploaded CSV file should contain the following columns.

| Column | Description |
|---------|-------------|
| CustomerID | Unique Customer ID |
| Gender | Male / Female |
| Age | Customer Age |
| Annual Income (k$) | Annual Income |
| Spending Score (1-100) | Spending Score |

Example

| CustomerID | Gender | Age | Annual Income (k$) | Spending Score (1-100) |
|------------|--------|-----|--------------------|------------------------|
| 1 | Male | 19 | 15 | 39 |
| 2 | Female | 24 | 16 | 81 |

---

# 🧠 Machine Learning Workflow

```
Dataset

↓

Data Cleaning

↓

Feature Selection

↓

Elbow Method

↓

Optimal K

↓

K-Means Clustering

↓

Customer Segments

↓

Visualization

↓

Reports
```

---

# 📈 Customer Segments

The system automatically groups customers into different segments such as:

- VIP Customers
- Platinum Customers
- Gold Customers
- Silver Customers
- Potential Customers
- Budget Customers
- Careful Customers

---

# 📊 Visualizations

The dashboard includes:

- Income Distribution
- Spending Score Distribution
- Gender Distribution
- Age Distribution
- Scatter Plot
- Cluster Visualization
- Elbow Curve
- Segment Statistics

---

# 📥 Export Options

Users can export reports in:

- CSV
- Excel
- PDF

---

# 🔐 Authentication

Registered users can:

- Login
- Access Dashboard
- Upload Dataset
- View Reports
- Logout

---

# Future Enhancements

- AI-Based Customer Recommendations
- Deep Learning Models
- Real-Time Dashboard
- Email Reports
- REST API
- Cloud Deployment
- PostgreSQL Database
- Role-Based Authentication
- Customer Prediction
- Dark Mode

---

# Screenshots

Add screenshots here.

```
Home Page

Dashboard

Analytics

Customers

Reports

Clustering

Settings
```

---

# Requirements

```
Python 3.13+

Django 6.x

Pandas

NumPy

Plotly

Scikit-learn

OpenPyXL

ReportLab
```

---

# Author

**Giridhar kalapala**

Junior Software Developer

---

# License

This project is developed for educational and academic purposes.

---

# Acknowledgements

- Django
- Scikit-learn
- Plotly
- Bootstrap
- Pandas
- NumPy

---

## ⭐ If you found this project useful, please consider giving it a star on GitHub.