from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.index,
        name="index"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "analytics/",
        views.analytics,
        name="analytics"
    ),

    path(
        "download/csv/",
        views.download_csv,
        name="download_csv"
    ),

    path(
        "download/excel/",
        views.download_excel,
        name="download_excel"
    ),

    path(
        "download/pdf/",
        views.download_pdf,
        name="download_pdf"
    ),

    path(
        "upload/",
        views.upload_dataset,
        name="upload_dataset"
    ),
    
    path(
        "customers/",
        views.customers,
        name="customers"
    ),

    path(
        "reports/",
        views.reports,
        name="reports"
    ),

    path(
        "settings/",
        views.settings,
        name="settings"
    ),


]