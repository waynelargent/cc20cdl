from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from . import forms
from .models import Narrative 
from .models import ELDT
from .models import PreTripInsp 
from .models import RoadSkills
from .models import BackingSkills
from .models import Attendance 
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

def backing_skills(request):
    if request.method == "POST":
        form = forms.CreateBackingSkills(request.POST)
        if form.is_valid():
            newrating = form.save(commit = False)
            newrating.instructor = request.user
            newrating.save()
            return redirect('/')
    else:
        form = forms.CreateBackingSkills()
    return render(request,'ratings/backing_skills.html', {'form': form})         
        
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

def instr_list_pre_trip(request):
    ratings = PreTripInsp.objects.all().order_by('-rating_date')
    return render(request, 'ratings/instr_list_pre_trip.html', {'ratings': ratings})

def instr_edit_pre_trip(request, pk):
    # 1. Fetch the existing record using the ID (pk) from the URL
    record = get_object_or_404(PreTripInsp, pk=pk)
    if request.method == 'POST':
        # 2. Bind data to the form, AND tell it which instance to update
        form = forms.CreatePreTripInsp(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/ratings/instr-list-pre-trip')
    else:
        # 3. GET request: Pre-fill the form with the existing data
        form = forms.CreatePreTripInsp(instance=record)
    return render(request, 'ratings/pre_trip_insp.html', {'form': form})

@login_required(login_url='/users/login') #applies to function underneath it
def pre_trip_insp(request):
    if request.method == "POST":
        form = forms.CreatePreTripInsp(request.POST)
        if form.is_valid():
            newrating = form.save(commit = False)
            newrating.instructor = request.user
            newrating.save()
            return redirect('/ratings/instr-list-pre-trip/')
    else:
        form = forms.CreatePreTripInsp()
    return render(request,'ratings/pre_trip_insp.html', {'form': form})


@login_required(login_url='/users/login') #applies to function underneath it
def eldt_and_score_sheet(request):
    if request.method == "POST":
        form = forms.CreateELDT(request.POST)   #Naming convention for EDLT Lesson Plan? 
        if form.is_valid():
            newrating = form.save(commit = False)
            newrating.instructor = request.user
            newrating.save()
            return redirect('/')
    else:
        form = forms.CreateELDT()
    return render(request,'ratings/eldt_and_score_sheet.html', {'form': form})


@login_required(login_url='/users/login')
def attendance(request):
    if request.method == "POST":
        form = forms.CreateAttendance(request.POST)
        if form.is_valid():
            newrating = form.save(commit = False)
            newrating.instructor = request.user
            newrating.save()
            return redirect('/')
    else:
        form = forms.CreateAttendance()
    return render(request,'ratings/attendance.html', {'form': form})