from django.db import models

from apps.account.models import Account
from apps.sanatorium.models import (DiagnosisTemplate, IllnessHistory)


class RepeatedAppointmentWithDoctorModel(models.Model):
    created_by = models.ForeignKey(Account, related_name='rawd_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_rawd", on_delete=models.SET_NULL, null=True)

    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    illness_history = models.ForeignKey(
        IllnessHistory, on_delete=models.CASCADE,
        null=True, related_name='repeated_appointment'
    )

    complaint = models.TextField(null=True, blank=True)
    objective_data = models.TextField(null=True, blank=True)

    arterial_high = models.IntegerField(null=True)
    arterial_low = models.IntegerField(null=True)
    imt = models.FloatField(null=True)

    diagnosis = models.ForeignKey(DiagnosisTemplate, null=True, on_delete=models.SET_NULL)
    cito = models.BooleanField(default=False)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class FinalAppointmentWithDoctorModel(models.Model):
    STATE_CHOICES = (
        ('assigned', 'assigned'),
        ('cancelled', 'cancelled'),
        ('stopped', 'stopped'),
        ('dispatched', 'dispatched'),
    )
    RESULT_CHOICES = (
        ('Улучение', 'Улучение'),
        ('Без изменения', 'Без изменения'),
        ('Ухудшение', 'Ухудшение'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=50, default='assigned')

    created_by = models.ForeignKey(Account, related_name='fawd_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_fawd", on_delete=models.SET_NULL, null=True)

    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    illness_history = models.ForeignKey(
        IllnessHistory, on_delete=models.CASCADE,
        null=True, related_name='final_appointment'
    )

    objective_status = models.TextField(null=True, blank=True)

    height = models.FloatField()
    weight = models.FloatField()
    heart_beat = models.IntegerField()
    arterial_high = models.IntegerField()
    arterial_low = models.IntegerField()
    imt = models.FloatField()
    imt_interpretation = models.FloatField()

    diagnosis = models.ManyToManyField(DiagnosisTemplate, null=True)
    summary = models.TextField(blank=True, null=True)

    treatment_results = models.CharField(choices=RESULT_CHOICES, max_length=50, default='Улучение')

    def __str__(self):
        return f"{self.id}"
