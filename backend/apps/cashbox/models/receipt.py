from django.db import models
from apps.account.models import ReferringDoctorModel, Account, SpecialityModel, MedicalService, PatientModel, \
    AppointmentsModel

PAYMENT_TYPE = (
    ("CASH", "CASH"),
    ("CARD", "CARD"),
)

TYPE = (
    ("INCOME", "INCOME"),
    ("OUTCOME", "OUTCOME"),
)


class ReceiptModel(models.Model):
    appointment = models.OneToOneField(AppointmentsModel, related_name='receipt', on_delete=models.SET_NULL, null=True)
    referring_doc = models.ForeignKey(ReferringDoctorModel, related_name='ref_receipt', on_delete=models.SET_NULL, null=True)

    created_by = models.ForeignKey(Account, related_name="crt_receipt", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_receipt", on_delete=models.SET_NULL, null=True)
    # operationist?


