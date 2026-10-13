from django.db import models

class EnergyRecord(models.Model):
    factory_name = models.CharField(max_length=150)

    consumption_kwh = models.DecimalField(
        max_digits=20,
        decimal_places=2,
    )

    recorded_date = models.DateField()

    def __str__(self):
        return self.factory_name