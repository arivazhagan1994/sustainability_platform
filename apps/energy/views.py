from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render

def energy_dashboard(request):
    data = {
        "consumption": 750,
    }

    return render(request, "energy/dashboard.html", data)

def energy_records(request):
    return HttpResponse(
        "Here you see the Energy records,"
    )

def add_energy(request):
    return HttpResponse(
        "Add a New Energy data here!"
    )

def energy_reports(request):
    return HttpResponse(
        "Energy Reports"
    )


