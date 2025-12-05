from django.urls import path
from . import views

app_name="ratings"
urlpatterns=[
    path("narrative/", views.narrative, name="narrative"),
    path("view-my-ratings/", views.view_my_ratings, name = "view-my-ratings"), #url is the same as the name
    path("road-skills/", views.road_skills, name="road-skills"),

    ]