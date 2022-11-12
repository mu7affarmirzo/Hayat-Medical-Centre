from django.db import models
from datetime import date, datetime, time, timedelta
from apps.account.models import ReferringDoctorModel, Account
from apps.account.models import BranchModel
from apps.account.models import PatientModel, InformationSourceModel
from apps.account.models import SpecialityModel
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

APPOINTMENT_CHOICES = (
    ('PAID', "PAID"),
    ('NOT PAID', "NOT PAID"),
    ('CANCELLED', "CANCELLED"),
)


class MedicalService(models.Model):
    name = models.CharField(max_length=255)
    cost = models.BigIntegerField()
    doctor = models.ManyToManyField(Account, blank=True)
    speciality = models.ForeignKey(SpecialityModel, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(Account, related_name='med_serv_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_med_serv", on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


class AppointmentsModel(models.Model):
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(choices=APPOINTMENT_CHOICES, default='NOT PAID', max_length=50)
    exemption = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    price = models.BigIntegerField()
    debt = models.BigIntegerField(default=0)
    referring_doctor = models.ForeignKey(ReferringDoctorModel, blank=True, null=True, on_delete=models.SET_NULL)
    information_source = models.ForeignKey(InformationSourceModel, blank=True, null=True, on_delete=models.SET_NULL)
    referring_doc_notes = models.TextField(blank=True, null=True)
    addition_info = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_appointment", on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.patient) + " - " + str(self.name)

    class Meta:
        ordering = ['-created_at']


class AppointmentServiceModel(models.Model):
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="app_serv", on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)
    appointment = models.ForeignKey(AppointmentsModel, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(MedicalService, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.service)


class EMCDocumentModel(models.Model):
    name = models.CharField(max_length=255)
    patient = models.ForeignKey(PatientModel, blank=True, null=True, on_delete=models.SET_NULL) #OneToOne ?
    service = models.ForeignKey(AppointmentServiceModel, on_delete=models.SET_NULL, null=True)
    appointment = models.ForeignKey(AppointmentsModel, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(Account, related_name='emc_doc_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name='emc_doc_modified', on_delete=models.SET_NULL, null=True)


@receiver(post_save, sender=AppointmentsModel)
def add_end_time(sender, instance=None, created=False, **kwargs):
    print(instance.start_time)
    if not instance.end_time:
        instance.end_time = instance.start_time + timedelta(minutes=30)

        instance.save()