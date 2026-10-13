from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .models import EnergyRecord

def energy_dashboard(request):
    data = {
        "consumption": 750,
    }

    return render(request, "energy/dashboard.html", data)

def energy_records(request):
    records = EnergyRecord.objects.all()
    return render (request, "energy/records.html",{"records":records})

def add_energy(request):
    return HttpResponse(
        "Add a New Energy data here!"
    )

def energy_reports(request):
    return render(request, "energy/reports.html")


