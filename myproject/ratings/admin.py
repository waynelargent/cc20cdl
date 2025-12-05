from django.contrib import admin
from .models import Narrative, BackingSkills
from .models import RoadSkills, PreTripInsp

# Register your models here.

admin.site.register(Narrative)
admin.site.register(BackingSkills)
admin.site.register(RoadSkills)
admin.site.register(PreTripInsp)
