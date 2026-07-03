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
