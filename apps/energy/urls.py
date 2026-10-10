from django.urls import path
from . import views

app_name = "energy"

urlpatterns = [
    path(
        "",
        views.energy_dashboard,
        name = "dashboard"
    ),
    path(
        "records/",
        views.energy_records,
        name = "records"
    ),
    path(
        "add/",
        views.add_energy,
        name = "add"
    ),

    path(
        "reports/",
        views.energy_reports,
        name = "reports"
    ),

]