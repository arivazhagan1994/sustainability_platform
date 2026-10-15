from django import forms
from .models import EnergyRecord

class EnergyRecordForm(forms.ModelForm):
    class meta:
        model = EnergyRecord

        fields = [
            "factory_name",
            "consumption_kwh",
            "recorded_date"
        ]