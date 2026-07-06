from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import plotly.express as px
import plotly.io as pio

from clustering.preprocessing import (
    load_dataset,
    dataset_summary,
    dataset_health
)

from clustering.analytics import create_charts
from clustering.kmeans import (
    perform_clustering,
    cluster_summary,
    elbow_method
)

from clustering.reports import (
    export_csv,
    export_excel,
    export_pdf
)

import pandas as pd
from django.core.files.storage import FileSystemStorage 

def index(request):
    return render(request, "pages/index.html")


@login_required
def dashboard(request):

    # Load dataset
    df = load_dataset()

    # -----------------------------
    # Apply Filters
    # -----------------------------
    gender = request.GET.get("gender")
    income = request.GET.get("income")
    spending = request.GET.get("spending")

    if gender:
        df = df[df["Gender"] == gender]

    if income:
        df = df[df["Annual_Income"] >= int(income)]

    if spending:
        df = df[df["Spending_Score"] >= int(spending)]

    # -----------------------------
    # Empty Dataset Check
    # -----------------------------
    if df.empty:

        return render(
            request,
            "pages/dashboard.html",
            {
                "error": "No customers found for the selected filters.",
                "customers": []
            }
        )

    # -----------------------------
    # Summary
    # -----------------------------
    summary = dataset_summary(df)

    health = dataset_health(df)

    # -----------------------------
    # Clustering
    # -----------------------------
    clustered_df, cluster_chart = perform_clustering(df)

    segment_summary = cluster_summary(clustered_df)

    # -----------------------------
    # Charts
    # -----------------------------
    income_chart = px.histogram(
        clustered_df,
        x="Annual_Income",
        title="Annual Income Distribution",
        color_discrete_sequence=["#2563EB"]
    )

    income_chart.update_layout(
        template="plotly_white",
        height=350
    )

    spending_chart = px.histogram(
        clustered_df,
        x="Spending_Score",
        title="Spending Score Distribution",
        color_discrete_sequence=["#10B981"]
    )

    spending_chart.update_layout(
        template="plotly_white",
        height=350
    )

    # -----------------------------
    # Context
    # -----------------------------
    context = {

        **summary,

        **health,

        "income_chart": pio.to_html(
            income_chart,
            full_html=False
        ),

        "spending_chart": pio.to_html(
            spending_chart,
            full_html=False
        ),

        "cluster_chart": cluster_chart,

        "customers": clustered_df.to_dict("records"),

        "segments": segment_summary.to_dict("records"),

    }

    return render(
        request,
        "pages/dashboard.html",
        context
    )

@login_required
def analytics(request):

    df = load_dataset()

    charts = create_charts(df)

    return render(
        request,
        "pages/analytics.html",
        charts
    )

@login_required
def download_csv(request):

    df = load_dataset()

    clustered_df, _ = perform_clustering(df)

    return export_csv(clustered_df)


@login_required
def download_excel(request):

    df = load_dataset()

    clustered_df, _ = perform_clustering(df)

    return export_excel(clustered_df)


@login_required
def download_pdf(request):

    df = load_dataset()

    clustered_df, _ = perform_clustering(df)

    return export_pdf(clustered_df)

@login_required
def upload_dataset(request):

    if request.method == "POST":

        uploaded_file = request.FILES["dataset"]

        storage = FileSystemStorage()

        filename = storage.save(uploaded_file.name, uploaded_file)

        file_path = storage.path(filename)

        df = pd.read_csv(file_path)

        df.rename(columns={
            "Annual Income (k$)": "Annual_Income",
            "Spending Score (1-100)": "Spending_Score"
        }, inplace=True)

        clustered_df, cluster_chart = perform_clustering(df)

        segment_summary = cluster_summary(clustered_df)

        context = {

            "customers": clustered_df.to_dict("records"),

            "cluster_chart": cluster_chart,

            "segments": segment_summary.to_dict("records")

        }

        return render(
            request,
            "pages/clustering.html",
            context
        )

    return render(
        request,
        "pages/upload_dataset.html"
    )

# ==============
@login_required
def customers(request):

    df = load_dataset()

    clustered_df, _ = perform_clustering(df)

    clustered_df["Membership"] = clustered_df["Annual_Income"].apply(
        lambda x: "VIP" if x >= 100
        else "Platinum" if x >= 80
        else "Gold" if x >= 50
        else "Silver"
    )

    clustered_df["Status"] = clustered_df["Spending_Score"].apply(
        lambda x: "Active" if x >= 50 else "Inactive"
    )

    context = {

        "customers": clustered_df.to_dict("records"),

        "total_customers": len(clustered_df),

        "male_count": len(
            clustered_df[clustered_df["Gender"]=="Male"]
        ),

        "female_count": len(
            clustered_df[clustered_df["Gender"]=="Female"]
        ),

        "vip_count": len(
            clustered_df[
                clustered_df["Segment"]=="VIP Customers"
            ]
        )

    }

    return render(
        request,
        "pages/customers.html",
        context
    )

# reports=====
@login_required
def reports(request):

    df = load_dataset()

    clustered_df, _ = perform_clustering(df)

    clustered_df["Membership"] = clustered_df["Annual_Income"].apply(
        lambda x: "VIP" if x >= 100
        else "Platinum" if x >= 80
        else "Gold" if x >= 50
        else "Silver"
    )

    context = {

        "total_customers": len(clustered_df),

        "average_income": round(
            clustered_df["Annual_Income"].mean(),2
        ),

        "average_spending": round(
            clustered_df["Spending_Score"].mean(),2
        ),

        "vip_count": len(
            clustered_df[
                clustered_df["Membership"]=="VIP"
            ]
        ),

        "segments": clustered_df["Segment"].nunique(),

    }

    return render(
        request,
        "pages/reports.html",
        context
    )

@login_required
def settings(request):

    context = {

        "username": request.user.username,

        "email": request.user.email,

        "project_name": "Customer Segmentation Using Clustering",

        "version": "1.0",

        "dataset": "Mall_Customers.csv"

    }

    return render(
        request,
        "pages/settings.html",
        context
    )