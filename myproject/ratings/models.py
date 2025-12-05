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

class BackingSkills(models.Model):
    student = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        limit_choices_to = {'groups__name' : 'students'}, #can only choose student
        related_name = 'student_backing_skills'
    )
    instructor = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default = None,
        related_name = 'instructor_backing_skills'
    )
    RATING_LEVEL = {
        1: "Level 1",
        2: "Level 2",
        3: "Level 3",
        4: "Level 4",
        5: "Level 5",
    }
    rating_date = models.DateField(default = timezone.now)
    btw_hours = models.FloatField()
    alley_dock = models.IntegerField(choices = RATING_LEVEL)
    straight_line = models.IntegerField(choices = RATING_LEVEL)
    off_set_backing_right = models.IntegerField(choices = RATING_LEVEL)
    off_set_backing_left = models.IntegerField(choices = RATING_LEVEL)
    parallel_park = models.IntegerField(choices = RATING_LEVEL)
    coupling = models.IntegerField(choices = RATING_LEVEL)
    uncoupling = models.IntegerField(choices = RATING_LEVEL)
    pull_ups = models.IntegerField(choices = RATING_LEVEL)
    encroachments = models.IntegerField(choices = RATING_LEVEL)
    instructor_approval = models.BooleanField(default = False)
    student_approval = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}" #grab students name from user table    