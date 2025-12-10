from django.urls import path
from . import views

app_name="ratings"
urlpatterns=[
    path("narrative/", views.narrative, name="narrative"),
    path("backing-skills/", views.backing_skills, name="backing-skills"),
    path("view-my-ratings/", views.view_my_ratings, name = "view-my-ratings"), #url is the same as the name
    path("pre-trip-insp/", views.pre_trip_insp, name="pre-trip-insp"),
    path("eldt-and-score-sheet/", views.eldt_and_score_sheet, name = "eldt-and-score-sheet"),
    path("road-skills/", views.road_skills, name="road-skills"),
    path("attendance/", views.attendance, name="attendance"),
    path("instr-list-pre-trip/", views.instr_list_pre_trip, name="instr-list-pre-trip"),
    # <int:pk> captures the ID from the URL and passes it to the view
    path('instr-edit-pre-trip/<int:pk>/', views.instr_edit_pre_trip, name='instr-edit-pre-trip'),
]
