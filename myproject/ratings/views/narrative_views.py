#12/10/2025
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .. import forms


from ..models import Narrative 


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


def view_my_ratings(request):
    ratings = Narrative.objects.filter(student = request.user).order_by('rating_date') #grab from narrative table and grab rows(object) for the logged in student
    return render(request, 'ratings/view_my_ratings.html', {'ratings': ratings})

def instr_list_narrative(request):
    ratings = Narrative.objects.all().order_by('-rating_date')
    return render(request, 'ratings/instr_list_narrative.html', {'ratings': ratings})

def instr_edit_narrative(request, pk):
    # 1. Fetch the existing record using the ID (pk) from the URL
    record = get_object_or_404(Narrative, pk=pk)
    if request.method == 'POST':
        # 2. Bind data to the form, AND tell it which instance to update
        form = forms.CreateNarrative(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/ratings/instr-list-narrative')
    else:
        # 3. GET request: Pre-fill the form with the existing data
        form = forms.CreateNarrative(instance=record)
    return render(request, 'ratings/instr_list_narrative.html', {'form': form})