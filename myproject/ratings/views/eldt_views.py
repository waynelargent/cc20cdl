#12/10/2025
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .. import forms

from ..models import ELDT

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