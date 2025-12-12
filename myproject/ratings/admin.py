from django.contrib import admin
from .models import Narrative
from .models import PreTripInsp
from .models import RoadSkills
from .models import ELDT
from .models import BackingSkills
from .models import Attendance
from .models import Trucks
from .models import CRN
from .models import Students

# Register your models here.

admin.site.register(Narrative)
admin.site.register(ELDT)
admin.site.register(BackingSkills)
admin.site.register(RoadSkills)
admin.site.register(PreTripInsp)
admin.site.register(Attendance)
admin.site.register(Trucks)
admin.site.register(CRN)
admin.site.register(Students)
