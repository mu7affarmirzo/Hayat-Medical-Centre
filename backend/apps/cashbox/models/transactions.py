from django.db import models

from apps.account.models import BranchModel, Account, ReferringDoctorModel
from apps.cashbox.models import ReceiptModel


PAYMENT_TYPE = (
    ("CASH", "CASH"),
    ("CARD", "CARD"),
    ("PAYME", "PAYME"),
    ("CLICK", "CLICK"),
)

TYPE = (
    ("INCOME", "INCOME"),
    ("OUTCOME", "OUTCOME"),
)


class TransactionsModel(models.Model):
    amount = models.BigIntegerField()
    payment_type = models.CharField(choices=PAYMENT_TYPE, max_length=50, default='CASH')
    is_manual = models.BooleanField(default=False)
    # bank_name = models.CharField(max_length=255, null=True, blank=True)
    receipt = models.ForeignKey(ReceiptModel, on_delete=models.SET_NULL, null=True)
    appointment_id = models.IntegerField(null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)
    transaction_type = models.CharField(choices=TYPE, max_length=50, default='INCOME')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, related_name="crt_transactions", on_delete=models.SET_NULL, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_transactions", on_delete=models.SET_NULL, null=True)
    referring_doctor = models.ForeignKey(ReferringDoctorModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.amount} - {self.payment_type}"

    # @property
    # def referring_doctor(self):
    #     # ref_doc_id = self.receipt.receipt_appointments.
    #     return 1


# @receiver(post_save, sender=TransactionsModel)
# def create_auth_token(sender, instance, created=False, **kwargs):
#     if not instance.is_manual:
#         appointment = AppointmentsModel.objects.get(id=instance.appointment_id)
#         instance.amount = appointment.price
#         instance.save()
