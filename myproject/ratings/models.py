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
    RATING_CHOICES = {                  #Value for Null? 
        0: " ",
        1: "Level 1", 
        2: "Level 2",
        3: "Level 3",
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
    in_cab_and_lights = models.IntegerField(verbose_name = "In-Cab & Exterior Lights", choices = RATING_CHOICES)
    brake_tests = models.IntegerField(choices = RATING_CHOICES)
    truck_side_rear = models.IntegerField(verbose_name = "Truck Side & Rear", choices = RATING_CHOICES)
    coupling_area = models.IntegerField(choices = RATING_CHOICES)
    drives_and_5th_wheel = models.IntegerField(verbose_name = "Drives & Fifth Wheel", choices = RATING_CHOICES)
    trailer_sides = models.IntegerField(verbose_name = "Trailer Sides & Cross-members",choices = RATING_CHOICES)
    trailer_tandems = models.IntegerField(choices = RATING_CHOICES)
    rear_of_trailer = models.IntegerField(choices = RATING_CHOICES) 
    student_approval = models.BooleanField(default = False)
    instructor_approval = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"

class ELDT(models.Model):
        CHAPTER = {                  #Value for Null? 
            1: "Chapter 1: Orientation", 
            2: "Chapter 2: Control Systems / Dashboard",
            3: "Chapter 3: Pre and Post - Trip Inspections",
            4: "Chapter 4: Basic Control", 
            5: "Chapter 5: Shifting / Operating Transmissions", 
            6: "Chapter 6: Backing and Docking", 
            7: "Chapter 7: Coupling and Uncoupling",
            8: "Chapter 8: Visual Search",
            9: "Chapter 9: Communication", 
            10: "Chapter 10: Distracted Driving",
            11: "Chapter 11: Speed Management", 
            12: "Chapter 12: Space Management",
            13: "Chapter 13: Night Operation",
            14: "Chapter 14: Extreme Driving Conditions", 
            15: "Chapter 15: Hazard Perception", 
            16: "Chapter 16: Skid Control / Recovery, Jackknifing and Other Emergencies", 
            17: "Chapter 17: Railroad - Highway Grade Crossings",
            18: "Chapter 18: Identification and Diagnosis of Malfunctions",
            19: "Chapter 19: Roadside Inspections", 
            20: "Chapter 20: Maintenence",
            21: "Chapter 21: Handling and Documenting Cargo", 
            22: "Chapter 22: Environmental Compliance Issues",
            23: "Chapter 23: Hours of Service Requirements",
            24: "Chapter 24: Fatigue and Wellness Awareness", 
            25: "Chapter 25: Post-Crash Procedures", 
            26: "Chapter 26: External Communications", 
            27: "Chapter 27: Whistleblower / Coercion",
            28: "Chapter 28: Trip Planning",
            29: "Chapter 29: Drugs / Alcohol", 
            30: "Chapter 30: Medical Requirements",    
            31: "Chapter 31: Human Trafficking",
            32: "Chapter 32: CSA Traffic Laws, FMCSR, PUCO", 
            33: "Final Exam Review",
            34: "Final Exam",

        # What should we put for "Final Exams, & Final Exam Review"? 
    
        } 
        student = models.ForeignKey(
            User, 
            on_delete = models.CASCADE,
            limit_choices_to = {'groups__name' : 'students'},
            related_name = 'student_eldt_and_score_sheet'
        )
        instructor = models.ForeignKey(
            User,
            on_delete = models.CASCADE,
            default = None,
            related_name = 'instructor_eldt_and_score_sheet'
        )
        # will need to add attendance and front half of lesson plan form
        chapter = models.IntegerField(verbose_name = "Select Chapter", choices = CHAPTER) #char field if we add "Final Exams, & Final Exam Review"?
        lesson_plan = models.TextField()
        score = models.IntegerField()
        # percentage = models.IntegerField() (Autocalculation?)
        student_approval = models.BooleanField(default = False)
        instructor_approval = models.BooleanField(default = False) # license Num.     


