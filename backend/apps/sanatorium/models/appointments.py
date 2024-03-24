from django.db import models

from apps.account.models import Account
from apps.sanatorium.models import (DiagnosisTemplate, IllnessHistory)


STATE_CHOICES = (
        ('assigned', 'assigned'),
        ('cancelled', 'cancelled'),
        ('stopped', 'stopped'),
        ('dispatched', 'dispatched'),
        ('dispatched', 'dispatched'),
    )


class ConsultingWithNeurologistModel(models.Model):
    ST_CHOICES = (
        ('Показан', 'Показан'),
        ('Не показан', 'Не показан'),
        ('Противопоказан', 'Противопоказан'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=50, default='assigned')

    created_by = models.ForeignKey(Account, related_name='cwn_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_cwn", on_delete=models.SET_NULL, null=True)

    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    illness_history = models.ForeignKey(
        IllnessHistory, on_delete=models.CASCADE,
        null=True, related_name='neurologist_consulting'
    )
    is_familiar_with_anamnesis = models.BooleanField(default=False)
    complaint = models.TextField(null=True, blank=True)
    anamnesis = models.TextField(null=True, blank=True)

    #
    #  OTHER FIELDS
    #

    cito = models.BooleanField(default=False)
    for_sanatorium_treatment = models.CharField(choices=ST_CHOICES, max_length=50, null=True, blank=True)
    summary = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class ConsultingWithCardiologistModel(models.Model):
    ST_CHOICES = (
        ('Показан', 'Показан'),
        ('Не показан', 'Не показан'),
        ('Противопоказан', 'Противопоказан'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=50, default='assigned')

    created_by = models.ForeignKey(Account, related_name='cw_cardio_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_cw_cardio", on_delete=models.SET_NULL, null=True)

    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    illness_history = models.ForeignKey(
        IllnessHistory, on_delete=models.CASCADE,
        null=True, related_name='cardiologist_consulting'
    )
    has_cardio_complaints = models.BooleanField(default=False)
    has_nerve_complaints = models.BooleanField(default=False)
    other_complaints = models.TextField(null=True, blank=True)
    anamnesis = models.TextField(null=True, blank=True)

    #
    #  OTHER FIELDS
    #

    cito = models.BooleanField(default=False)
    for_sanatorium_treatment = models.CharField(choices=ST_CHOICES, max_length=50, null=True, blank=True)
    summary = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class AppointmentWithOnDutyDoctorModel(models.Model):
    ST_CHOICES = (
        ('Показан', 'Показан'),
        ('Не показан', 'Не показан'),
        ('Противопоказан', 'Противопоказан'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=50, default='assigned')

    created_by = models.ForeignKey(Account, related_name='aw_on_duty_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_aw_on_duty", on_delete=models.SET_NULL, null=True)

    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    illness_history = models.ForeignKey(
        IllnessHistory, on_delete=models.CASCADE,
        null=True, related_name='on_duty_doctor_appointment'
    )
    complaints = models.TextField(null=True, blank=True)
    objective_data = models.TextField(null=True, blank=True)

    arterial_high = models.IntegerField(null=True)
    arterial_low = models.IntegerField(null=True)
    imt = models.FloatField(null=True)

    cito = models.BooleanField(default=False)
    for_sanatorium_treatment = models.CharField(choices=ST_CHOICES, max_length=50, null=True, blank=True)
    summary = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class RepeatedAppointmentWithDoctorModel(models.Model):

    state = models.CharField(choices=STATE_CHOICES, max_length=50, default='assigned')

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
