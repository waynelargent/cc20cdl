from django.contrib import admin
from .models import Narrative, PreTripInsp, ELDT

# Register your models here.

admin.site.register(Narrative)

admin.site.register(PreTripInsp)

admin.site.register(ELDT)