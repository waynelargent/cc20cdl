#12/10/2025
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .. import forms

from ..models import BackingSkills


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


def instr_list_backing_skills(request):
    ratings = BackingSkills.objects.all().order_by('-rating_date')
    return render(request, 'ratings/instr_list_backing_skills.html', {'ratings': ratings})

def instr_edit_backing_skills(request, pk):
    # 1. Fetch the existing record using the ID (pk) from the URL
    record = get_object_or_404(BackingSkills, pk=pk)
    if request.method == 'POST':
        # 2. Bind data to the form, AND tell it which instance to update
        form = forms.CreateBackingSkills(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/ratings/instr-list-backing-skills')
    else:
        # 3. GET request: Pre-fill the form with the existing data
        form = forms.CreateBackingSkills(instance=record)
    return render(request, 'ratings/backing_skills.html', {'form': form})


