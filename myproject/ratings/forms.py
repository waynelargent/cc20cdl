from django import forms
from . import models


class CreateNarrative(forms.ModelForm):
    class Meta:
        model = models.Narrative
        fields = ['student', 'narrative', 'student_approval', 'instructor_approval']

class CreateBackingSkills(forms.ModelForm):
    class Meta:
        model = models.BackingSkills
        fields = ['student', 'btw_hours', 'alley_dock', 'straight_line', 'off_set_backing_right', 'off_set_backing_left', 'parallel_park', 'coupling', 'uncoupling', 'pull_ups', 'encroachments', 'student_approval', 'instructor_approval']
        