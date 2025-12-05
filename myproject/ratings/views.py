from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from . import forms
from .models import Narrative, RoadSkills, PreTripInsp


# Create your views here.

@login_required(login_url='/users/login') #applies to function underneath it
def narrative(request):
    if request.method == "POST":
        form = forms.CreateNarrative(request.POST)
        if form.is_valid():
            newrating = form.save(commit = False)
            newrating.instructor = request.user
            newrating.save()
            return redirect('/')
    else:
        form = forms.CreateNarrative()
    return render(request,'ratings/narrative.html', {'form': form})

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

def view_my_ratings(request):
    ratings = Narrative.objects.filter(student = request.user).order_by('rating_date') #grab from narrative table and grab rows(object) for the logged in student
    return render(request, 'ratings/view_my_ratings.html', {'ratings': ratings})

@login_required(login_url='/users/login') #applies to function underneath it
def pre_trip_insp(request):
    if request.method == "POST":
        form = forms.CreatePreTripInsp(request.POST)
        if form.is_valid():
            newrating = form.save(commit = False)
            newrating.instructor = request.user
            newrating.save()
            return redirect('/')
    else:
        form = forms.CreatePreTripInsp()
    return render(request,'ratings/pre_trip_insp.html', {'form': form})
