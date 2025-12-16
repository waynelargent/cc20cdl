#12/10/2025
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .. import forms
from django.contrib.auth.models import User, Group   # for student filter

from ..models import Attendance 


@login_required(login_url='/users/login')
def attendance(request):
    if request.method == "POST":
        form = forms.CreateAttendance(request.POST)
        if form.is_valid():
            newrating = form.save(commit = False)
            newrating.instructor = request.user
            newrating.save()
            return redirect('/ratings/instr-list-attendance/')
    else:
        form = forms.CreateAttendance()
    return render(request,'ratings/attendance.html', {'form': form})

def instr_list_attendance(request):
    students = User.objects.filter(groups__name='students')
    selected_student_id = request.GET.get('student_id')
    ratings = Attendance.objects.all().order_by('-rating_date')
    if selected_student_id:
        ratings = ratings.filter(student_id=selected_student_id)
        context = {
            'students': students,
            'ratings': ratings,
            'selected_student_id': selected_student_id,
        }
    return render(request, 'ratings/instr_list_attendance.html', context)

def instr_edit_attendance(request, pk):
    # 1. Fetch the existing record using the ID (pk) from the URL
    record = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        # 2. Bind data to the form, AND tell it which instance to update
        form = forms.CreateAttendance(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/ratings/instr-list-attendance')
    else:
        # 3. GET request: Pre-fill the form with the existing data
        form = forms.CreateAttendance(instance=record)
    return render(request, 'ratings/attendance.html', {'form': form})