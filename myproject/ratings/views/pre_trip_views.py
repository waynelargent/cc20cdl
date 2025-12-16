#12/10/2025
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .. import forms
from django.contrib.auth.models import User, Group   # for student filter

from ..models import PreTripInsp 

# rating entry form
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

# instructor list of pre-trip-insp ratings
def instr_list_pre_trip(request):
    # 1. Get all users in the 'students' group for the dropdown
    students = User.objects.filter(groups__name='students')
    # 2. Get the selected student ID from the URL (GET request)
    selected_student_id = request.GET.get('student_id')
    # 3. Filter ratings if an ID is provided
    ratings = PreTripInsp.objects.all().order_by('rating_date')  # original query
    if selected_student_id:
        ratings = ratings.filter(student_id=selected_student_id)  # where does student_id come from?
    # put all the data in a dictionary so it can be passed to the HTML file
    context = {
        'students': students,
        'ratings': ratings,
        'selected_student_id': selected_student_id,
    }
    return render(request, 'ratings/instr_list_pre_trip.html', context)

# form for editing an existing record    
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

def student_list_pre_trip(request):
    ratings = PreTripInsp.objects.filter(student = request.user).order_by('-rating_date') 
    return render(request, 'ratings/student_list_pre_trip.html', {'ratings': ratings})
