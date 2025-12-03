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

    