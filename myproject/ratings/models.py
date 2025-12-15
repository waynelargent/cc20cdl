from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Trucks(models.Model):
    TRUCK_CHOICES = { 
        "School Bus" : "School Bus",
        "Trailor" : "Trailor",
        "Straight" : "Straight",
        "Tractor" : "Tractor",
        "Pulled Trailor" : "Pulled Trailor",
    }
    truck_num = models.CharField()
    truck_type = models.CharField(choices = TRUCK_CHOICES)
    truck_description = models.TextField(null = True)

    def __str__(self):
        return f"{self.truck_num} {self.truck_type}"


class CRN(models.Model):
    crn = models.CharField()
    semester = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField() # to be calculated as startdate +270 days
    active = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.crn} {self.semester}"


class Students(models.Model):
    student_id= models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"groups__name": "students"}        
    )
    crn = models.ForeignKey(
        CRN,
        on_delete=models.CASCADE        
    )
    sphone = models.CharField()
    active = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.student_id}"

class Narrative(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"groups__name": "students"},  # can only choose student
        related_name="student_narrative",
    )
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        related_name="instructor_narrative",
    )
    rating_date = models.DateField(default=timezone.now)
    narrative = models.TextField()
    instructor_approval = models.BooleanField(default=False)
    student_approval = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"

    # grab students name from user table


class BackingSkills(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"groups__name": "students"},  # can only choose student
        related_name="student_backing_skills",
    )
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        related_name="instructor_backing_skills",
    )
    RATING_LEVEL = {
        0: " ",
        1: "Level 1",
        2: "Level 2",
        3: "Level 3",
        4: "Level 4",
        5: "Level 5",
    }
    rating_date = models.DateField(default=timezone.now)
    btw_hours = models.FloatField()
    alley_dock = models.IntegerField(choices=RATING_LEVEL, default = 0)
    straight_line = models.IntegerField(choices=RATING_LEVEL, default = 0)
    off_set_backing_right = models.IntegerField(choices=RATING_LEVEL, default = 0)
    off_set_backing_left = models.IntegerField(choices=RATING_LEVEL, default = 0)
    parallel_park = models.IntegerField(choices=RATING_LEVEL, default = 0)
    coupling = models.IntegerField(choices=RATING_LEVEL, default = 0)
    uncoupling = models.IntegerField(choices=RATING_LEVEL, default = 0)
    pull_ups = models.IntegerField(choices=RATING_LEVEL, default = 0)
    encroachments = models.IntegerField(choices=RATING_LEVEL, default = 0)
    instructor_approval = models.BooleanField(default=False)
    student_approval = models.BooleanField(default=False)

def __str__(self): 
    return f"{self.student.first_name} {self.student.last_name}"  # grab students name from user table


class RoadSkills(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"groups__name": "students"},
        related_name="student_road_skills",
    )
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        related_name="instructor_road_skills",
    )   
    RATING_LEVEL = {
        0: " ",
        1: "Level 1",
        2: "Level 2",
        3: "Level 3",
        4: "Level 4",
        5: "Level 5",
    }
    rating_date = models.DateField(default=timezone.now)
    truck_num = models.ForeignKey(
        Trucks,
        on_delete=models.CASCADE   
    )
    acceleration = models.IntegerField(choices=RATING_LEVEL, default = 0)
    braking = models.IntegerField(choices=RATING_LEVEL, default = 0)
    steering = models.IntegerField(choices=RATING_LEVEL, default = 0)
    shifting = models.IntegerField(choices=RATING_LEVEL, default = 0)
    rturn_approach = models.IntegerField(choices=RATING_LEVEL, default = 0)
    rturn_turning = models.IntegerField(choices=RATING_LEVEL, default = 0)
    rturn_complete_turn = models.IntegerField(choices=RATING_LEVEL, default = 0)
    rturn_signal_use = models.IntegerField(choices=RATING_LEVEL, default = 0)
    lturn_approach = models.IntegerField(choices=RATING_LEVEL, default = 0)
    lturn_turning = models.IntegerField(choices=RATING_LEVEL, default = 0)
    lturn_complete_turn = models.IntegerField(choices=RATING_LEVEL, default = 0)
    lturn_signal_use = models.IntegerField(choices=RATING_LEVEL, default = 0)
    lane_control = models.IntegerField(choices=RATING_LEVEL, default = 0)
    smooth_braking = models.IntegerField(choices=RATING_LEVEL, default = 0)
    proper_stop = models.IntegerField(choices=RATING_LEVEL, default = 0)
    proper_mirror = models.IntegerField(choices=RATING_LEVEL, default = 0)
    enter_interstate = models.IntegerField(choices=RATING_LEVEL, default = 0)
    proper_lane_change = models.IntegerField(choices=RATING_LEVEL, default = 0)
    speed_following_distance = models.IntegerField(choices=RATING_LEVEL, default = 0)
    exit_interstate = models.IntegerField(choices=RATING_LEVEL, default = 0)
    railroad_approach = models.IntegerField(choices=RATING_LEVEL, default = 0)
    railroad_crossing = models.IntegerField(choices=RATING_LEVEL, default = 0)
    railroad_completion = models.IntegerField(choices=RATING_LEVEL, default = 0)
    pull_over_deceleration = models.IntegerField(choices=RATING_LEVEL, default = 0)
    pull_over_smooth = models.IntegerField(choices=RATING_LEVEL, default = 0)
    pull_over_re_entry = models.IntegerField(choices=RATING_LEVEL, default = 0)
    recognize_traffic_hazards = models.IntegerField(choices=RATING_LEVEL, default = 0)
    recognize_ohead_hazards = models.IntegerField(choices=RATING_LEVEL, default = 0)
    obey_laws = models.IntegerField(choices=RATING_LEVEL, default = 0)
    smith_system_defensive_driving = models.IntegerField(choices=RATING_LEVEL, default = 0)
    btw_hours = models.FloatField()
    student_approval = models.BooleanField(default=False)
    instructor_approval = models.BooleanField(default=False)


def __str__(self):
    return f"{self.student.first_name} {self.student.last_name}"


class PreTripInsp(models.Model):
    RATING_CHOICES = {  # Value for Null?
        0: " ",
        1: "Level 1",
        2: "Level 2",
        3: "Level 3",
        4: "Level 4",
        5: "Level 5",
    }
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={
            "groups__name": "students",
            "students__active": True },
        related_name="student_pre_trip_insp",
    )
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        related_name="instructor_pre_trip_insp",
    )
    rating_date = models.DateField(default=timezone.now)  # this may change later
    training_hours_today = models.FloatField()
    engine_compartment = models.IntegerField(choices=RATING_CHOICES, default = 0)
    in_cab_and_lights = models.IntegerField(
        verbose_name="In-Cab & Exterior Lights", choices=RATING_CHOICES, default = 0
    )
    brake_tests = models.IntegerField(choices=RATING_CHOICES, default = 0)
    truck_side_rear = models.IntegerField(
        verbose_name="Truck Side & Rear", choices=RATING_CHOICES, default = 0
    )
    coupling_area = models.IntegerField(choices=RATING_CHOICES, default = 0)
    drives_and_5th_wheel = models.IntegerField(
        verbose_name="Drives & Fifth Wheel", choices=RATING_CHOICES, default = 0
    )
    trailer_sides = models.IntegerField(
        verbose_name="Trailer Sides & Cross-members", choices=RATING_CHOICES, default = 0
    )
    trailer_tandems = models.IntegerField(choices=RATING_CHOICES, default = 0)
    rear_of_trailer = models.IntegerField(choices=RATING_CHOICES, default = 0)
    student_approval = models.BooleanField(default=False)
    instructor_approval = models.BooleanField(default=False)

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
        

class Attendance(models.Model):
    student = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        limit_choices_to = {'groups__name' : 'students'}, #can only choose student
        related_name = 'student_attendance'
    )
    instructor = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default = None,
        related_name = 'instructor_attendance'
    )
    rating_date = models.DateField(default = timezone.now) #do i put the forms.DateInput here?
    time_in = models.TimeField()
    break_am_out = models.TimeField(null = True, blank = True)
    break_am_in = models.TimeField(null = True, blank = True)
    lunch_out = models.TimeField(null = True, blank = True)
    lunch_in = models.TimeField(null = True, blank = True)
    break_pm_out = models.TimeField(null = True, blank = True)
    break_pm_in = models.TimeField(null = True, blank = True)
    time_out = models.TimeField()
    instructor_approval = models.BooleanField(default = False)
    student_approval = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}" 
    #grab students name from user table             
