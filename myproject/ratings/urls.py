from django.urls import path
from . import views

app_name="ratings"
urlpatterns=[
    path("narrative/", views.narrative, name="narrative"),
    path("backing-skills/", views.backing_skills, name="backing-skills"),
    
    path("pre-trip-insp/", views.pre_trip_insp, name="pre-trip-insp"),

    # added eldt instr list and edit list 
    path("eldt-and-score-sheet/", views.eldt_and_score_sheet, name = "eldt-and-score-sheet"),
    path("instr-list-eldt/", views.instr_list_eldt, name="instr-list-eldt"),
    path('instr-edit-eldt/<int:pk>/', views.instr_edit_eldt, name='instr-edit-eldt'),
    
    path("road-skills/", views.road_skills, name="road-skills"),

    # added attendance instr list and edit list 
    path("attendance/", views.attendance, name="attendance"),
    path("instr-list-attendance/", views.instr_list_attendance, name="instr-list-attendance"),
    path('instr-edit-attendance/<int:pk>/', views.instr_edit_attendance, name='instr-edit-attendance'),

    path("instr-list-pre-trip/", views.instr_list_pre_trip, name="instr-list-pre-trip"),
    # <int:pk> captures the ID from the URL and passes it to the view
    path('instr-edit-pre-trip/<int:pk>/', views.instr_edit_pre_trip, name='instr-edit-pre-trip'),
    path("instr-list-road-skills/", views.instr_list_road_skills, name="instr-list-road-skills"),
    # <int:pk> captures the ID from the URL and passes it to the view
    path('instr-edit-road-skills/<int:pk>/', views.instr_edit_road_skills, name='instr-edit-road-skills'),
    path("instr-list-backing-skills/", views.instr_list_backing_skills, name="instr-list-backing-skills"),
    path("instr-edit-backing-skills/<int:pk>/", views.instr_edit_backing_skills, name="instr-edit-backing-skills"),
    path("instr-list-narrative/", views.instr_list_narrative, name="instr-list-narrative"),
    path('instr-edit-narrative/<int:pk>/', views.instr_edit_narrative, name='instr-edit-narrative'),

    path("student-list-pre-trip/", views.student_list_pre_trip, name = "student-list-pre-trip"), 
    path("student-list-attendance/", views.student_list_attendance, name = "student-list-attendance"),
    path("student-list-narrative/", views.student_list_narrative, name = "student-list-narrative"),

]









