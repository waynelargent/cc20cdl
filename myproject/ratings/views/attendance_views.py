#12/10/2025
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .. import forms


from ..models import Attendance 


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