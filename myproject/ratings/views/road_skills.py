from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .. import forms


from ..models import RoadSkills


def road_skills(request):
    if request.method == "POST":
        form = forms.CreateRoadSkills(request.POST)
        if form.is_valid():
            newrating = form.save(commit = False)
            newrating.instructor = request.user
            newrating.save()
            return redirect('/')
    else:
        form = forms.CreateRoadSkills()
    return render(request, 'ratings/road_skills.html', {'form': form})