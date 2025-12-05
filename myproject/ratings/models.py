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
        return f"{self.student.first_name} {self.student.last_name}" #grab students name from user table

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