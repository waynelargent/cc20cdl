#12/10/2025
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .. import forms

from ..models import PreTripInsp 

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