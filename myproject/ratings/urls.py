from django.urls import path
from . import views

app_name="ratings"
urlpatterns=[
    path("narrative/", views.narrative, name="narrative"),
    path("view-my-ratings/", views.view_my_ratings, name = "view-my-ratings"), #url is the same as the name
    path("pre-trip-insp/",views.pre_trip_insp, name="pre-trip-insp")
]