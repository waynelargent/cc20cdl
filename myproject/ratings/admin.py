from django.contrib import admin
from .models import Narrative
from .models import PreTripInsp
from .models import RoadSkills
from .models import ELDT
from .models import BackingSkills

# Register your models here.

admin.site.register(Narrative)
admin.site.register(ELDT)
admin.site.register(BackingSkills)
admin.site.register(RoadSkills)
admin.site.register(PreTripInsp)
