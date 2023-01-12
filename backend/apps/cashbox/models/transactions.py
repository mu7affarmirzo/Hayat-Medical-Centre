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


class DutyModel(models.Model):
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, related_name="duty", on_delete=models.SET_NULL, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_duty", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.created_at} - {self.created_by}- {self.is_closed}"

    def close_the_duty(self):
        self.is_closed = True
        self.save()

    class Meta:
        ordering = ('-created_at', )
        verbose_name_plural = 'CASHBOX| 1. Duty'
        verbose_name = 'CASHBOX| 1. Duty'


class TransactionsModel(models.Model):
    duty = models.ForeignKey(DutyModel, on_delete=models.SET_NULL, null=True)
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


class AppointmentServiceTransactionsModel(models.Model):
    transaction = models.ForeignKey(TransactionsModel, on_delete=models.SET_NULL, null=True, related_name='tr_srv')
    service_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.transaction} - {self.service_id}"
