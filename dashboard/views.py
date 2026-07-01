from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import plotly.express as px
from django.conf import settings
import plotly.io as pio
import pandas as pd
import os

def index(request):
    return render(request, "pages/index.html")


@login_required
def dashboard(request):

    # Dummy data (We'll replace this with CSV data later)
    df = pd.DataFrame({

        "CustomerID":[1001,1002,1003,1004,1005],

        "Gender":[
            "Male",
            "Female",
            "Female",
            "Male",
            "Female"
        ],

        "Age":[22,31,28,40,35],

        "Income":[40000,75000,52000,68000,90000],

        "Spending":[65,89,52,70,95],

        "Cluster":[
            "Cluster 1",
            "Cluster 2",
            "Cluster 1",
            "Cluster 3",
            "Cluster 2"
        ]

    })

    income_chart = px.bar(
        df,
        x="Income",
        y="Spending",
        title="Income vs Spending"
    )

    age_chart = px.histogram(
        df,
        x="Age",
        title="Age Distribution"
    )

    context = {

        "income_chart":pio.to_html(
            income_chart,
            full_html=False
        ),

        "age_chart":pio.to_html(
            age_chart,
            full_html=False
        ),

    }

    return render(
        request,
        "pages/dashboard.html",
        context
    )