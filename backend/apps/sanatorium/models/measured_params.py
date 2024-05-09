from django.db import models

from apps.account.models import Account
from apps.sanatorium.models import IllnessHistory


class ArterialPressureModel(models.Model):
    illness_history = models.ForeignKey(IllnessHistory, on_delete=models.CASCADE,
                                        null=True, related_name='arterial_pressure')
    systologic = models.FloatField(null=True, blank=True)
    diastologic = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(Account, related_name='arterial_pressure_created', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.systologic} {self.diastologic}"


class GlucometerModel(models.Model):
    illness_history = models.ForeignKey(IllnessHistory, on_delete=models.CASCADE,
                                        null=True, related_name='glucometer_model')
    blood_glucose = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(Account, related_name='glucometer_created', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.blood_glucose} {self.date}"


class PulseModel(models.Model):
    illness_history = models.ForeignKey(IllnessHistory, on_delete=models.CASCADE,
                                        null=True, related_name='pulse_model')
    pulse = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(Account, related_name='pulse_created', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pulse} {self.date}"


class SaturationModel(models.Model):
    illness_history = models.ForeignKey(IllnessHistory, on_delete=models.CASCADE,
                                        null=True, related_name='saturation_model')
    saturation = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(Account, related_name='saturation_created', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.saturation} {self.date}"


class TemperatureModel(models.Model):
    illness_history = models.ForeignKey(IllnessHistory, on_delete=models.CASCADE,
                                        null=True, related_name='temperature')
    temperature = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(Account, related_name='temperature_created', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.temperature} {self.date}"
