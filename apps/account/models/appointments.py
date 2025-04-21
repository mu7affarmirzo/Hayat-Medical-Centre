import uuid

from django.db import models
from datetime import date, datetime, time, timedelta
from apps.account.models import ReferringDoctorModel, Account, DoctorAccountModel
from apps.account.models import BranchModel
from apps.account.models import PatientModel, InformationSourceModel
from apps.account.models import SpecialityModel
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from apps.cashbox.models import ReceiptModel

APPOINTMENT_CHOICES = (
    ('PAID', "PAID"),
    ('NOT PAID', "NOT PAID"),
    ('CANCELLED', "CANCELLED"),
    ('CANCELLED CANCELLED', "CANCELLED CANCELLED"),
)


class MedicalServiceCategory(models.Model):
    # consulting
    # instrumental research
    # laboratory research
    name = models.CharField(max_length=255, null=False, blank=False)

    created_by = models.ForeignKey(Account, related_name='med_serv_category_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_med_serv_category", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


class MedicalService(models.Model):
    TYPES = (
        ("service", "service"),
        ("procedure", "procedure"),
        ("consulting", "consulting")
    )
    name = models.CharField(max_length=255)
    cost = models.BigIntegerField()
    doctor = models.ManyToManyField(DoctorAccountModel, blank=True)
    speciality = models.ForeignKey(SpecialityModel, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='med_service_specialty')
    """
    look at sanatorium 
    https://www.figma.com/file/aeByA9WSTeHdobGPmKAxfR/Hayat-Medical-(Project)?type=design&node-id=3595-18579&mode=design&t=5d8fgNQjEiyO1W9h-0
    """
    category = models.ForeignKey(MedicalServiceCategory, on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=TYPES, default="service", max_length=50, null=True)

    created_by = models.ForeignKey(Account, related_name='med_serv_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_med_serv", on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


class AppointmentsModel(models.Model):
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    # receipt = models.ForeignKey(ReceiptModel, blank=True, null=True, on_delete=models.SET_NULL,
    #                             related_name='receipt_appointments')
    doctor = models.ForeignKey(DoctorAccountModel, blank=True, null=True, on_delete=models.SET_NULL,
                               related_name='doctor_appointments')
    name = models.CharField(max_length=255, blank=True, null=True)

    discount = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    referring_doctor = models.ForeignKey(ReferringDoctorModel, blank=True, null=True, on_delete=models.SET_NULL)
    information_source = models.ForeignKey(InformationSourceModel, blank=True, null=True, on_delete=models.SET_NULL)
    referring_doc_notes = models.TextField(blank=True, null=True)
    addition_info = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(null=True, blank=True)
    is_manual = models.BooleanField(default=True, null=True)
    is_contract = models.BooleanField(default=False, null=True)
    is_priority = models.BooleanField(default=False, null=True)  # makes it priority in queue
    send_sms = models.BooleanField(default=False, null=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_appointment", on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.patient) + " - " + str(self.name) + " - " + str(self.doctor)

    # @property
    # def price(self):
    #     total_price = 0
    #     services = self.app_services.all()
    #     for service in services:
    #         price = service.service.cost * service.quantity
    #         total_price += price
    #     return total_price

    @property
    def debt(self):
        total_debt = 0
        services = self.app_services.all()
        for service in services:
            if service.payment_status not in ['PAID', 'CANCELLED CANCELLED']:
                total_debt += service.service.cost
        return total_debt

    class Meta:
        ordering = ['-created_at']


class ContractModel(models.Model):
    contract_number = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.contract_number) + " - " + str(self.policy_number)

    class Meta:
        ordering = ['-created_at']


class AppointmentServiceModel(models.Model):
    payment_status = models.CharField(choices=APPOINTMENT_CHOICES, default='NOT PAID', max_length=50)
    has_proceed = models.BooleanField(default=False)

    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="app_serv", on_delete=models.SET_NULL, null=True)
    appointment = models.ForeignKey(AppointmentsModel, related_name='app_services', on_delete=models.SET_NULL,
                                    null=True)
    service = models.ForeignKey(MedicalService, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.service)


class EMCDocumentModel(models.Model):
    name = models.CharField(max_length=255)
    patient = models.ForeignKey(PatientModel, blank=True, null=True, on_delete=models.SET_NULL)  # OneToOne ?
    service = models.ForeignKey(AppointmentServiceModel, on_delete=models.SET_NULL, null=True)
    appointment = models.ForeignKey(AppointmentsModel, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(Account, related_name='emc_doc_created', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name='emc_doc_modified', on_delete=models.SET_NULL, null=True)


@receiver(post_save, sender=AppointmentsModel)
def add_end_time(sender, instance=None, created=False, **kwargs):
    if not instance.end_time:
        instance.end_time = instance.start_time + timedelta(minutes=30)

        instance.save()
