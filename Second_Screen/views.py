from django.shortcuts import render, redirect
from .models import ParkingList
from .forms import ParkingListForm


def login(request):
    return render(request, 'login.html', {'title': 'Registration'})


def park_list(request):
    error = ''
    if request.method == 'POST':
        form = ParkingListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('park_list')
        else:
            error = 'form is not valid!'
            return redirect('park_list')
    form = ParkingListForm()
    context = {
        'form': form,
        'error': error
    }
    parking = ParkingList.objects.all()
    return render(request, 'park_list.html', {'title': 'Change the Parking places', 'listHelper': parking})


def manager(request):
    parking = ParkingList.objects.all()
    return render(request, 'manager.html', {'title': 'Change the Parking places', 'listHelper': parking})


def worker(request):
    parking = ParkingList.objects.all()
    return render(request, 'worker.html', {'title': 'List of Parking places', 'listHelper': parking})
