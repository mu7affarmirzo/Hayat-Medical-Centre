from django.db import models
from apps.account.models import ReferringDoctorModel, Account, SpecialityModel, MedicalService, PatientModel

PAYMENT_TYPE = (
    ("CASH", "CASH"),
    ("CARD", "CARD"),
                )
TYPE = (
    ("INCOME", "INCOME"),
    ("OUTCOME", "OUTCOME"),
                )


class ReceiptModel(models.Model):
    referring_doctor = models.ForeignKey(ReferringDoctorModel, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_receipt", on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    specialty = models.ForeignKey(SpecialityModel, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(MedicalService, on_delete=models.SET_NULL, null=True)
    payment_type = models.CharField(max_length=30, default="CASH", choices=PAYMENT_TYPE)
    patient = models.ForeignKey(PatientModel, on_delete=models.SET_NULL, null=True)
    base_price = models.BigIntegerField()
    paid_amount = models.BigIntegerField()
    note = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    type = models.CharField(max_length=30, choices=True)
    # operationist?
    