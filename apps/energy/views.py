from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .models import EnergyRecord
from .views import EnergyRecordForm

def energy_dashboard(request):
    data = {
        "consumption": 750,
    }

    return render(request, "energy/dashboard.html", data)

def energy_records(request):
    records = EnergyRecord.objects.all()
    return render (request, "energy/records.html",{"records":records})

def add_energy(request):
    form = EnergyRecordForm()

    return render(
        request,
        "energy/add_energy.html",
        {"form":form}
    )

def energy_reports(request):
    return render(request, "energy/reports.html")


