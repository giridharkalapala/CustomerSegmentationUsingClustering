import os
import pandas as pd
from django.conf import settings


def load_dataset():

    csv_path = os.path.join(
        settings.BASE_DIR,
        "dataset",
        "Mall_Customers.csv"
    )

    df = pd.read_csv(csv_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Rename columns
    df.rename(columns={
        "Annual Income (k$)": "Annual_Income",
        "Spending Score (1-100)": "Spending_Score"
    }, inplace=True)

    return df


def dataset_summary(df):

    return {

        "total_customers": len(df),

        "average_income": round(
            df["Annual_Income"].mean(), 2
        ),

        "average_spending": round(
            df["Spending_Score"].mean(), 2
        ),

        "male_count": len(
            df[df["Gender"] == "Male"]
        ),

        "female_count": len(
            df[df["Gender"] == "Female"]
        ),

    }

def dataset_health(df):

    return {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "missing_values": int(df.isnull().sum().sum()),

        "duplicate_records": int(df.duplicated().sum()),

        "memory_usage": round(df.memory_usage(deep=True).sum() / 1024, 2),

    }   