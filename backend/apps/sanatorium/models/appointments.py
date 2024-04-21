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

    diagnosis = models.ManyToManyField(DiagnosisTemplate)
    summary = models.TextField(blank=True, null=True)

    treatment_results = models.CharField(choices=RESULT_CHOICES, max_length=50, default='Улучение')

    def __str__(self):
        return f"{self.id}"


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
    palpebral_fissures = models.CharField(max_length=50, null=True, blank=True)  # Глазные щели
    pupils = models.CharField(max_length=50, null=True, blank=True)
    reaction_on_pupils = models.CharField(max_length=50, null=True, blank=True)
    aye_frame_movement = models.CharField(max_length=50, null=True, blank=True)
    nystagmus = models.CharField(max_length=50, null=True, blank=True)
    face = models.CharField(max_length=50, null=True, blank=True)
    tongue = models.CharField(max_length=50, null=True, blank=True)
    soft_sk = models.CharField(max_length=50, null=True, blank=True)
    phonation_swallowing = models.CharField(max_length=50, null=True, blank=True)
    reflexes = models.CharField(max_length=50, null=True, blank=True)
    muscle_strength = models.CharField(max_length=50, null=True, blank=True)
    muscle_tones = models.CharField(max_length=50, null=True, blank=True)
    deep_reflexes_hand = models.CharField(max_length=50, null=True, blank=True)
    deep_reflexes_foot = models.CharField(max_length=50, null=True, blank=True)
    stylo_radial = models.CharField(max_length=50, null=True, blank=True)
    
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


class AppointmentWithOnDutyDoctorOnArrivalModel(models.Model):
    ST_CHOICES = (
        ('Показан', 'Показан'),
        ('Не показан', 'Не показан'),
        ('Противопоказан', 'Противопоказан'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=50, default='assigned')

    created_by = models.ForeignKey(Account, related_name='aw_on_duty_on_arr_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_aw_on_duty_on_arr", on_delete=models.SET_NULL, null=True)

    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    illness_history = models.ForeignKey(
        IllnessHistory, on_delete=models.CASCADE,
        null=True, related_name='on_duty_doctor_on_arr_appointment'
    )
    complaints = models.TextField(null=True, blank=True)
    arv_number = models.CharField(null=True, blank=True, max_length=255)
    ayes_shells = models.CharField(null=True, blank=True, max_length=255)
    from_to_sanatorium = models.CharField(null=True, blank=True, max_length=255)
    road_crossed = models.CharField(null=True, blank=True, max_length=255)

    abroad_for_last_years = models.CharField(null=True, blank=True, max_length=255)
    virus_hepatitis = models.CharField(null=True, blank=True, max_length=255)
    tuberculosis = models.CharField(null=True, blank=True, max_length=255)
    malarias = models.CharField(null=True, blank=True, max_length=255)
    venerian_illness = models.CharField(null=True, blank=True, max_length=255)
    dizanteri = models.CharField(null=True, blank=True, max_length=255)
    helminthic_infestations = models.CharField(null=True, blank=True, max_length=255)
    had_contact_with_inf_people = models.CharField(null=True, blank=True, max_length=255)
    had_stul_for = models.BooleanField(default=False)

    allergy = models.CharField(null=True, blank=True, max_length=255)
    meteolabilisis = models.CharField(null=True, blank=True, max_length=255)
    non_carrying_prods = models.CharField(null=True, blank=True, max_length=255)
    stull_issues = models.CharField(null=True, blank=True, max_length=255)
    has_always_pills = models.CharField(null=True, blank=True, max_length=255)

    objective_data = models.TextField(null=True, blank=True)

    temperature = models.FloatField(null=True, blank=True)

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


class EkgAppointmentModel(models.Model):
    AXIS_CHOICES = (
        ('N', 'N'),
        ('горизонтальная', 'горизонтальная'),
        ('вертикальная', 'вертикальная'),
        ('отклонена влево', 'отклонена влево'),
        ('отклонена вправо', 'отклонена вправо')
    )

    ST_CHOICES = (
        ('Показан', 'Показан'),
        ('Не показан', 'Не показан'),
        ('Противопоказан', 'Противопоказан'),
    )

    state = models.CharField(choices=STATE_CHOICES, max_length=50, default='assigned')

    created_by = models.ForeignKey(Account, related_name='ekg_app_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_ekg_app", on_delete=models.SET_NULL, null=True)

    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    illness_history = models.ForeignKey(
        IllnessHistory, on_delete=models.CASCADE,
        null=True, related_name='ekg_app'
    )

    rhythm = models.CharField(max_length=50, null=True, blank=True)
    heart_s_count = models.IntegerField(null=True, blank=True)
    r_r = models.FloatField(null=True, blank=True)
    p_q = models.FloatField(null=True, blank=True)
    qrs = models.FloatField(null=True, blank=True)
    v1 = models.FloatField(null=True, blank=True)
    v6 = models.FloatField(null=True, blank=True)
    q_t = models.FloatField(null=True, blank=True)
    la = models.FloatField(null=True, blank=True)

    prong_p = models.CharField(max_length=50, null=True, blank=True)
    complex_qrs = models.CharField(max_length=50, null=True, blank=True)
    prong_t = models.CharField(max_length=50, null=True, blank=True)
    segment_st = models.CharField(max_length=50, null=True, blank=True)
    electric_axis = models.CharField(choices=AXIS_CHOICES, max_length=50, null=True, blank=True)

    cito = models.BooleanField(default=False)
    diagnosis = models.ForeignKey(DiagnosisTemplate, null=True, on_delete=models.SET_NULL)
    for_sanatorium_treatment = models.CharField(choices=ST_CHOICES, max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
