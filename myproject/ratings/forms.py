from django import forms
from . import models


class CreateNarrative(forms.ModelForm):
    class Meta:
        model = models.Narrative
        fields = ['student', 'narrative', 'student_approval', 'instructor_approval']