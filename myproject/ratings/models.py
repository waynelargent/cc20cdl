from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Narrative(models.Model):
    student = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        limit_choices_to = {'groups__name' : 'students'}, #can only choose student
        related_name = 'student_narrative'
    )
    instructor = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default = None,
        related_name = 'instructor_narrative'
    )
    rating_date = models.DateField(default = timezone.now)
    narrative = models.TextField()
    instructor_approval = models.BooleanField(default = False)
    student_approval = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}" 
    #grab students name from user table

class RoadSkills(models.Model):
    student = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        limit_choices_to = {'groups__name' : 'students'},
        related_name = 'student_road_skills'
    )
    instructor = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default = None,
        related_name = 'instructor_road_skills'
    )
    RATING_LEVEL = {
        1: 'Level 1',
        2: 'Level 2',
        3: 'Level 3',
        4: 'Level 4',
        5: 'Level 5',
    }
    rating_date = models.DateField(default = timezone.now)
    truck_num = models.IntegerField(verbose_name="Truck number")
    acceleration = models.IntegerField(choices = RATING_LEVEL)
    braking = models.IntegerField(choices = RATING_LEVEL)
    steering = models.IntegerField(choices = RATING_LEVEL)
    shifting = models.IntegerField(choices = RATING_LEVEL)
    rturn_approach = models.IntegerField(choices = RATING_LEVEL)
    rturn_turning = models.IntegerField(choices = RATING_LEVEL)
    rturn_complete_turn = models.IntegerField(choices = RATING_LEVEL)
    rturn_signal_use = models.IntegerField(choices = RATING_LEVEL)
    lturn_approach = models.IntegerField(choices = RATING_LEVEL)
    lturn_turning = models.IntegerField(choices = RATING_LEVEL)
    lturn_complete_turn = models.IntegerField(choices = RATING_LEVEL)
    lturn_signal_use = models.IntegerField(choices = RATING_LEVEL)
    lane_control = models.IntegerField(choices = RATING_LEVEL)
    smooth_braking = models.IntegerField(choices = RATING_LEVEL)
    proper_stop = models.IntegerField(choices = RATING_LEVEL)
    proper_mirror = models.IntegerField(choices = RATING_LEVEL)
    enter_interstate = models.IntegerField(choices = RATING_LEVEL)
    proper_lane_change = models.IntegerField(choices = RATING_LEVEL)
    speed_following_distance = models.IntegerField(choices = RATING_LEVEL)
    exit_interstate = models.IntegerField(choices = RATING_LEVEL)
    railroad_approach = models.IntegerField(choices = RATING_LEVEL)
    railroad_crossing = models.IntegerField(choices = RATING_LEVEL)
    railroad_completion = models.IntegerField(choices = RATING_LEVEL)
    pull_over_deceleration = models.IntegerField(choices = RATING_LEVEL)
    pull_over_smooth = models.IntegerField(choices = RATING_LEVEL)
    pull_over_re_entry = models.IntegerField(choices = RATING_LEVEL)
    recognize_traffic_hazards = models.IntegerField(choices = RATING_LEVEL)
    recognize_ohead_hazards = models.IntegerField(choices = RATING_LEVEL)
    obey_laws = models.IntegerField(choices = RATING_LEVEL)
    smith_system_defensive_driving = models.IntegerField(choices = RATING_LEVEL)
    btw_hours = models.FloatField()
    student_approval = models.BooleanField(default = False)
    instructor_approval = models.BooleanField(default = False)
    
    
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}" 








class PreTripInsp(models.Model):
    RATING_CHOICES = {
        1: "Level 1", 
        2: "Level 2",
        3:  "Level 3",
        4: "Level 4", 
        5: "Level 5", 
    } 
    student = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        limit_choices_to = {'groups__name' : 'students'},
        related_name = 'student_pre_trip_insp'
    )
    instructor = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default = None,
        related_name = 'instructor_pre_trip_insp'
    )
    rating_date = models.DateField(default = timezone.now) #this may change later
    training_hours_today = models.FloatField()
    engine_compartment = models.IntegerField(choices = RATING_CHOICES)
    in_cab_and_lights = models.IntegerField(choices = RATING_CHOICES)
    brake_tests = models.IntegerField(choices = RATING_CHOICES)
    truck_side_rear = models.IntegerField(choices = RATING_CHOICES)
    coupling_area = models.IntegerField(choices = RATING_CHOICES)
    drives_and_5th_wheel = models.IntegerField(verbose_name = "Drives & Fifth Wheel", choices = RATING_CHOICES)
    trailer_sides = models.IntegerField(choices = RATING_CHOICES)
    trailer_tandems = models.IntegerField(choices = RATING_CHOICES)
    rear_of_trailer = models.IntegerField(choices = RATING_CHOICES) 
    student_approval = models.BooleanField(default = False)
    instructor_approval = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"