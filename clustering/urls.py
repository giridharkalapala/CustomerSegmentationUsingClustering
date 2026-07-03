from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.clustering,
        name="clustering"
    ),

    path(
        "elbow/",
        views.elbow,
        name="elbow"
    ),

]