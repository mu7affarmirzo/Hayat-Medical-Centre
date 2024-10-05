from django.db import models

from apps.account.models import Account
from apps.lis.models import upload_location
from apps.sanatorium.models import (DiagnosisTemplate, IllnessHistory)


STATE_CHOICES = (
        ('Приём завершён', 'Приём завершён'),
        ('Пациент на прием не явился', 'Пациент на прием не явился'),
        ('Не завершено', 'Не завершено'),
    )


class FinalAppointmentWithDoctorModel(models.Model):

    RESULT_CHOICES = (
        ('Улучение', 'Улучение'),
        ('Без изменения', 'Без изменения'),
        ('Ухудшение', 'Ухудшение'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=250, default='Приём завершён')

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
    file = models.FileField(upload_to=upload_location, null=True, blank=True)

    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    heart_beat = models.IntegerField(null=True, blank=True)
    arterial_high_low = models.CharField(max_length=255, null=True, blank=True)
    arterial_high = models.IntegerField(null=True, blank=True)
    arterial_low = models.IntegerField(null=True, blank=True)
    imt = models.FloatField(null=True, blank=True)
    imt_interpretation = models.FloatField(null=True, blank=True)

    diagnosis = models.ManyToManyField(DiagnosisTemplate)
    summary = models.TextField(blank=True, null=True)

    treatment_results = models.CharField(choices=RESULT_CHOICES, max_length=250, default='Улучение')

    def __str__(self):
        return f"{self.id}"


class ConsultingWithNeurologistModel(models.Model):
    ST_CHOICES = (
        ('Показан', 'Показан'),
        ('Не показан', 'Не показан'),
        ('Противопоказан', 'Противопоказан'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=250, default='Приём завершён')

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

    palpebral_fissures = models.CharField(max_length=250, null=True, blank=True)  # Глазные щели
    pupils = models.CharField(max_length=250, null=True, blank=True)
    reaction_on_pupils = models.CharField(max_length=250, null=True, blank=True)
    aye_frame_movement = models.CharField(max_length=250, null=True, blank=True)
    nystagmus = models.CharField(max_length=250, null=True, blank=True)
    face = models.CharField(max_length=250, null=True, blank=True)
    tongue = models.CharField(max_length=250, null=True, blank=True)
    soft_sk = models.CharField(max_length=250, null=True, blank=True)
    phonation_swallowing = models.CharField(max_length=250, null=True, blank=True)
    reflexes = models.CharField(max_length=250, null=True, blank=True)
    muscle_strength = models.CharField(max_length=250, null=True, blank=True)
    muscle_tones = models.CharField(max_length=250, null=True, blank=True)
    deep_reflexes_hand = models.CharField(max_length=250, null=True, blank=True)
    deep_reflexes_foot = models.CharField(max_length=250, null=True, blank=True)
    stylo_radial = models.CharField(max_length=250, null=True, blank=True)
    biceps = models.CharField(max_length=250, null=True, blank=True, verbose_name='с двуглавой мышцы плеча')
    triceps = models.CharField(max_length=250, null=True, blank=True, verbose_name='с трехглавой мышцы плеча')
    knees = models.CharField(max_length=250, null=True, blank=True, verbose_name='коленные')
    achilles = models.CharField(max_length=250, null=True, blank=True, verbose_name='ахилловы')
    abdominal = models.CharField(max_length=250, null=True, blank=True, verbose_name='брюшные')
    pathological_reflexes = models.CharField(max_length=250, null=True, blank=True, verbose_name='Патологические рефлексы')
    romberg_position = models.CharField(
        max_length=250, null=True, blank=True,
        default='устойчив', verbose_name='Положение в позе Ромберга')
    complicated_position = models.CharField(
        max_length=250, null=True, blank=True,
        default='устойчив', verbose_name='В усложненной позе Ромберга')
    finger_test = models.CharField(
        max_length=250, null=True, blank=True,
        default='выполняет точно', verbose_name='Пальценосовая проба')
    heel_knee_test = models.CharField(
        max_length=250, null=True, blank=True,
        default='выполняет точно', verbose_name='Пяточно-коленная проба')
    gait = models.CharField(
        max_length=250, null=True, blank=True,
        default='устойчив', verbose_name='Походка')
    sensitivity = models.CharField(default='не нарушена', max_length=255)
    cognitive_test = models.CharField(null=True, blank=True, max_length=255)
    emotional_volitional_sphere = models.CharField(null=True, blank=True, max_length=255)
    insomnia = models.CharField(null=True, blank=True, max_length=255, default='эпизодическая')
    movements_in_the_cervical_spine = models.CharField(null=True, blank=True, max_length=255)
    movements_in_the_spinal_spine = models.CharField(
        null=True, blank=True, max_length=255, verbose_name='Движения в поясничном отделе позвоночника')
    spinous_processes = models.CharField(
        null=True, blank=True, max_length=255, verbose_name='Болезненность при пальпации остистых отростков')
    paravertebral_points = models.CharField(
        null=True, blank=True, max_length=255, verbose_name='Болезненность паравертебральных точек')
    lasegues_symptom = models.CharField(null=True, blank=True, max_length=255)

    cito = models.BooleanField(default=False)
    for_sanatorium_treatment = models.CharField(choices=ST_CHOICES, max_length=250, null=True, blank=True)
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
    BODY_CHOICES = (
        ('правильное,', 'правильное,'),
        ('неправильное,', 'неправильное,'),
        ('астеник', 'астеник'),
        ('нормастеник', 'нормастеник'),
        ('гиперстеник', 'гиперстеник'),
    )
    SKIN_CHOICES = (
        ('нормальной окраски', 'нормальной окраски'),
        ('бледные', 'бледные'),
        ('желтушные', 'желтушные'),
        ('гиперемированные,', 'гиперемированные,'),
        ('высыпания', 'высыпания'),
    )
    MUCOSA_CHOICES = (
        ('нормальной окраски', 'нормальной окраски'),
        ('бледные', 'бледные'),
        ('желтушные', 'желтушные'),
        ('гиперемированные,', 'гиперемированные,'),
    )
    THYROIDS_CHOICES = (
        ('не увеличена', 'не увеличена'),
        ('увеличена до', 'увеличена до'),
        ('0', '0'),
        ('I', 'I'),
        ('II ст', 'II ст'),
    )
    LYMPHATIC_CHOICES = (
        ('не увеличены', 'не увеличены'),
        ('увеличены', 'увеличены'),
        ('мягкие', 'мягкие'),
        ('уплотнены при пальпации', 'уплотнены при пальпации'),
        ('безболезненные', 'безболезненные'),
        ('болезненные', 'болезненные'),
    )

    PULSE_CHOICES = (
        ('ритмичный', 'ритмичный'),
        ('аритмичный', 'аритмичный'),
        ('напряжен', 'напряжен'),
        ('хорошего', 'хорошего'),
        ('удовлетворительного наполнения и напряжения', 'удовлетворительного наполнения и напряжения'),
    )
    HEART_TONE_CHOICES = (
        ('чистые', 'чистые'),
        ('ясные', 'ясные'),
        ('громкие', 'громкие'),
        ('приглушенные', 'приглушенные'),
        ('глухие', 'глухие'),
    )
    I_TONE_CHOICES = (
        ('ослаблен', 'ослаблен'),
        ('усилен', 'усилен'),
    )
    II_TONE_CHOICES = (
        ('аорте', 'аорте'),
        ('легочной артерии', 'легочной артерии'),
    )
    NOISE_CHOICES = (
        ('отсутствует', 'отсутствует'),
        ('диастолический', 'диастолический'),
    )
    ARTERIAL_PULSE_STOP_CHOICES = (
        ('отчетливая', 'отчетливая'),
        ('ослаблена', 'ослаблена'),
        ('отсутствует', 'отсутствует'),
        ('слева', 'слева'),
        ('справа', 'справа'),
    )
    SUPERFICIAL_VEINS_CHOICES = (
        ('отсутствует', 'отсутствует'),
        ('слева', 'слева'),
        ('справа', 'справа'),
    )
    CHEST_SHAPE_CHOICES = (
        ('правильная', 'правильная'),
        ('неправильная', 'неправильная'),
        ('«бочкообразная»', '«бочкообразная»'),
    )
    PULMONARY_FIELDS_CHOICES = (
        ('легочный', 'легочный'),
        ('с коробочным оттенком', 'с коробочным оттенком'),
        ('укорочение', 'укорочение'),
        ('притупление', 'притупление'),
    )
    AUSCULTATION_BREATHING_CHOICES = (
        ('везикулярное', 'везикулярное'),
        ('ослабленное', 'ослабленное'),
        ('жесткое', 'жесткое'),
        ('бронхиальное', 'бронхиальное'),
    )
    WHEEZING_CHOICES = (
        ('отсутствуют', 'отсутствуют'),
        ('имеются сухие', 'имеются сухие'),
        ('влажные', 'влажные'),
        ('крепитирующие', 'крепитирующие'),
    )
    PLEURAL_FRICTION_RUB_CHOICES = (
        ('шум трения плевры', 'шум трения плевры'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=250, default='Приём завершён')

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
    history_of_illness = models.TextField(null=True, blank=True)
    inheritance = models.TextField(null=True, blank=True)

    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    pulse_general = models.IntegerField(null=True, blank=True)
    arterial_high_low = models.CharField(max_length=255, null=True, blank=True)
    arterial_high = models.IntegerField(null=True, blank=True)
    arterial_low = models.IntegerField(null=True, blank=True)
    imt = models.FloatField(null=True, blank=True)
    imt_interpretation = models.FloatField(null=True, blank=True)

    body_figure = models.CharField(max_length=255, choices=BODY_CHOICES, default='правильное, нормастеник')
    skin = models.CharField(max_length=255, choices=SKIN_CHOICES, default='нормальной окраски')
    sclera_visible_mucosa = models.CharField(max_length=255, choices=MUCOSA_CHOICES, default='нормальной окраски')
    thyroids = models.CharField(max_length=255, choices=THYROIDS_CHOICES, default='не увеличена')
    cervical = models.CharField(max_length=255, choices=LYMPHATIC_CHOICES, default='не увеличены, мягкие, безболезненные')
    axillary = models.CharField(max_length=255, choices=LYMPHATIC_CHOICES, default='не увеличены, мягкие, безболезненные')
    inguinal = models.CharField(max_length=255, choices=LYMPHATIC_CHOICES, default='не увеличены, мягкие, безболезненные')

    pulse_per_min = models.IntegerField(null=True, blank=True)
    pulse = models.CharField(max_length=255, choices=PULSE_CHOICES, default='ритмичный')
    fault_of_pulse = models.CharField(max_length=255, default='отсутствует')
    heart_arterial_high = models.IntegerField(null=True, blank=True)
    heart_arterial_low = models.IntegerField(null=True, blank=True)
    left_heart_edges = models.CharField(max_length=255, default='в норме')
    right_heart_edges = models.CharField(max_length=255, default='в норме')
    upper_heart_edges = models.CharField(max_length=255, default='в норме')
    heart_beat = models.CharField(max_length=255, default='в норме')
    heart_tone = models.CharField(max_length=255, choices=HEART_TONE_CHOICES, default='чистые, ясные')
    i_tone = models.CharField(max_length=255, choices=I_TONE_CHOICES, null=True, blank=True)
    ii_tone = models.CharField(max_length=255, choices=II_TONE_CHOICES, null=True, blank=True)

    noise = models.CharField(max_length=255, choices=II_TONE_CHOICES, null=True, blank=True)
    arterial_pulse_stop = models.CharField(max_length=255, choices=ARTERIAL_PULSE_STOP_CHOICES, null=True, blank=True)
    varicose_veins_of_superficial_veins = models.CharField(max_length=255, choices=SUPERFICIAL_VEINS_CHOICES, default='отсутствует')
    trophic_skin_changes = models.CharField(max_length=255, default='отсутствует')

    chdd_per_minute = models.IntegerField(null=True, blank=True)
    chest_shape = models.CharField(max_length=255, choices=CHEST_SHAPE_CHOICES, default='правильная')
    pulmonary_fields = models.CharField(max_length=255,
        verbose_name='При сравнительной перкуссии над легочными полями звук',
        choices=PULMONARY_FIELDS_CHOICES, default='легочный'
    )
    auscultation_breathing = models.CharField(max_length=255,
        verbose_name='При аускультации дыхание',
        choices=AUSCULTATION_BREATHING_CHOICES, default='везикулярное,'
    )
    wheezing = models.CharField(max_length=255,
        verbose_name='Хрипы',
        choices=WHEEZING_CHOICES, default='везикулярное,'
    )
    pleural_friction_rub = models.CharField(max_length=255,
        verbose_name='шум трения плевры', null=True, blank=True,
        choices=PLEURAL_FRICTION_RUB_CHOICES
    )

    cito = models.BooleanField(default=False)
    file = models.FileField(upload_to=upload_location, null=True, blank=True)
    for_sanatorium_treatment = models.CharField(choices=ST_CHOICES, max_length=250, null=True, blank=True)
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
    PULSE_CHOICES = (
        ('ритмичный', 'ритмичный'),
        ('аритмичный', 'аритмичный'),
    )
    REGIME_CHOICES = (
        ('Щадящий', 'Щадящий'),
        ('Постельный', 'Постельный'),
        ('Тонизирующий', 'Тонизирующий'),
        ('Тренирующий', 'Тренирующий'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=250, default='Приём завершён')

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
    imt = models.IntegerField(null=True)

    pulse = models.CharField(choices=PULSE_CHOICES, null=True, blank=True, max_length=255)
    diet = models.CharField(null=True, blank=True, max_length=255)
    regime = models.CharField(choices=REGIME_CHOICES, null=True, blank=True, max_length=255)

    def __str__(self):
        return f"{self.id}"


class RepeatedAppointmentWithDoctorModel(models.Model):

    state = models.CharField(choices=STATE_CHOICES, max_length=250, default='Приём завершён')

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
    state = models.CharField(choices=STATE_CHOICES, max_length=250, default='Приём завершён')

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
    for_sanatorium_treatment = models.CharField(choices=ST_CHOICES, max_length=250, null=True, blank=True)
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

    state = models.CharField(choices=STATE_CHOICES, max_length=250, default='Приём завершён')

    created_by = models.ForeignKey(Account, related_name='ekg_app_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_ekg_app", on_delete=models.SET_NULL, null=True)

    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    illness_history = models.ForeignKey(
        IllnessHistory, on_delete=models.CASCADE,
        null=True, related_name='ekg_app'
    )

    rhythm = models.CharField(max_length=250, null=True, blank=True)
    heart_s_count = models.IntegerField(null=True, blank=True)
    r_r = models.FloatField(null=True, blank=True)
    p_q = models.FloatField(null=True, blank=True)
    qrs = models.FloatField(null=True, blank=True)
    v1 = models.FloatField(null=True, blank=True)
    v6 = models.FloatField(null=True, blank=True)
    q_t = models.FloatField(null=True, blank=True)
    la = models.FloatField(null=True, blank=True)

    prong_p = models.CharField(max_length=250, null=True, blank=True)
    complex_qrs = models.CharField(max_length=250, null=True, blank=True)
    prong_t = models.CharField(max_length=250, null=True, blank=True)
    segment_st = models.CharField(max_length=250, null=True, blank=True)
    electric_axis = models.CharField(choices=AXIS_CHOICES, max_length=250, null=True, blank=True)

    cito = models.BooleanField(default=False)
    diagnosis = models.ForeignKey(DiagnosisTemplate, null=True, on_delete=models.SET_NULL)
    for_sanatorium_treatment = models.CharField(choices=ST_CHOICES, max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
