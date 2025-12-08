from django import forms
from . import models


class CreateNarrative(forms.ModelForm):
    class Meta:
        model = models.Narrative
        fields = ['student', 'narrative', 'student_approval', 'instructor_approval']

class CreatePreTripInsp(forms.ModelForm):
    class Meta:
        model = models.PreTripInsp
        fields = [
           'student',  'training_hours_today', 
            'engine_compartment', 'in_cab_and_lights', 'brake_tests',
            'truck_side_rear', 'coupling_area', 'drives_and_5th_wheel',
            'trailer_sides', 'trailer_tandems', 'rear_of_trailer', 'student_approval', 'instructor_approval'
            ]

# Ask about date? Training hours total? Instructor License num?

class CreateELDT(forms.ModelForm):
    class Meta:
        model = models.ELDT
        fields = [
           'student',  'chapter', 
            'lesson_plan', 'score',
            'student_approval', 'instructor_approval'
            ]