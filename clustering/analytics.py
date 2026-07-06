# clustering/analytics.py

import plotly.express as px
import plotly.io as pio


def create_charts(df):

    charts = {}

    # Age Distribution
    age_fig = px.histogram(
        df,
        x="Age",
        title="Age Distribution",
        color_discrete_sequence=["#2563EB"]
    )
    age_fig.update_layout(template="plotly_white", height=350)
    charts["age_chart"] = pio.to_html(age_fig, full_html=False)

    # Gender Distribution
    gender_fig = px.pie(
        df,
        names="Gender",
        title="Gender Distribution"
    )
    gender_fig.update_layout(height=350)
    charts["gender_chart"] = pio.to_html(gender_fig, full_html=False)

    # Income Distribution
    income_fig = px.histogram(
        df,
        x="Annual_Income",
        title="Annual Income Distribution",
        color_discrete_sequence=["#10B981"]
    )
    income_fig.update_layout(template="plotly_white", height=350)
    charts["income_chart"] = pio.to_html(income_fig, full_html=False)

    # Spending Distribution
    spending_fig = px.histogram(
        df,
        x="Spending_Score",
        title="Spending Score Distribution",
        color_discrete_sequence=["#F59E0B"]
    )
    spending_fig.update_layout(template="plotly_white", height=350)
    charts["spending_chart"] = pio.to_html(spending_fig, full_html=False)

    # Income vs Spending
    scatter_fig = px.scatter(
        df,
        x="Annual_Income",
        y="Spending_Score",
        color="Gender",
        title="Income vs Spending"
    )
    scatter_fig.update_layout(template="plotly_white", height=450)
    charts["scatter_chart"] = pio.to_html(scatter_fig, full_html=False)

    # ==========================
    # Customer Statistics
    # ==========================

    if "Segment" in df.columns:

        cluster_count = (
            df["Segment"]
            .value_counts()
            .reset_index()
        )

        cluster_count.columns = [
            "Segment",
            "Customers"
        ]

        segment_chart = px.bar(
            cluster_count,
            x="Segment",
            y="Customers",
            color="Segment",
            title="Customers by Segment"
        )

        segment_chart.update_layout(
            template="plotly_white",
            height=450
        )

        charts["segment_chart"] = pio.to_html(
            segment_chart,
            full_html=False
        )

    return charts