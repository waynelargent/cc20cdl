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
        

class CreateRoadSkills(forms.ModelForm):
    class Meta:
        model = models.RoadSkills
        fields = ['student', 'truck_num', 'acceleration', 'braking', 'steering', 'shifting', 'rturn_approach', 'rturn_turning', 'rturn_complete_turn', 'rturn_signal_use', 'lturn_approach', 'lturn_turning', 'lturn_complete_turn', 'lturn_signal_use', 'lane_control', 'smooth_braking', 'proper_stop', 'proper_mirror', 'enter_interstate', 'proper_lane_change', 'speed_following_distance', 'exit_interstate', 'railroad_approach', 'railroad_crossing', 'railroad_completion', 'pull_over_deceleration', 'pull_over_smooth', 'pull_over_re_entry', 'recognize_traffic_hazards', 'recognize_ohead_hazards', 'obey_laws', 'smith_system_defensive_driving', 'btw_hours', 'student_approval', 'instructor_approval']
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
        

class CreateAttendance(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = [
            'student', 'rating_date', 'time_in',
            'break_am_out', 'break_am_in',
            'lunch_out', 'lunch_in',
            'break_pm_out', 'break_pm_in', 'time_out',
            'student_approval', 'instructor_approval'
            ]
        widgets = {
            'rating_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}, 
                format='%Y-%m-%d'
            ),
            'time_in':  forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}, 
                format='%H:%M'
            ),
            'break_am_out':  forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}, 
                format='%H:%M'
            ),
            'break_am_in':  forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}, 
                format='%H:%M'
            ),
            'lunch_out':  forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}, 
                format='%H:%M'
            ),
            'lunch_in':  forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}, 
                format='%H:%M'
            ),
            'break_pm_out':  forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}, 
                format='%H:%M'
            ),
            'break_pm_in':  forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}, 
                format='%H:%M'
            ),
            'time_out':  forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}, 
                format='%H:%M'
            ),
        }