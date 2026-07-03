from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .preprocessing import load_dataset
from .kmeans import (
    perform_clustering,
    cluster_summary,
    elbow_method
)


@login_required
def clustering(request):

    df = load_dataset()

    clustered_df, cluster_chart = perform_clustering(df)

    segment_summary = cluster_summary(clustered_df)

    context = {

        "cluster_chart": cluster_chart,

        "customers": clustered_df.to_dict("records"),

        "segments": segment_summary.to_dict("records"),

    }

    return render(
        request,
        "pages/clustering.html",
        context
    )


@login_required
def elbow(request):

    df = load_dataset()

    context = {

        "elbow_chart": elbow_method(df)

    }

    return render(
        request,
        "pages/elbow.html",
        context
    )