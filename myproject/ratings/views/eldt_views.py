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
            return redirect('/ratings/instr-list-eldt/')
    else:
        form = forms.CreateELDT()
    return render(request,'ratings/eldt_and_score_sheet.html', {'form': form})

def instr_list_eldt(request):
    ratings = ELDT.objects.all().order_by('chapter')
    return render(request, 'ratings/instr_list_eldt.html', {'ratings': ratings})

def instr_edit_eldt(request, pk):
    # 1. Fetch the existing record using the ID (pk) from the URL
    record = get_object_or_404(ELDT, pk=pk)
    if request.method == 'POST':
        # 2. Bind data to the form, AND tell it which instance to update
        form = forms.CreateELDT(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/ratings/instr-list-eldt')
    else:
        # 3. GET request: Pre-fill the form with the existing data
        form = forms.CreateELDT(instance=record)
    return render(request, 'ratings/eldt_and_score_sheet.html', {'form': form})