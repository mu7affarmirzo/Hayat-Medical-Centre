from django.db import models
from apps.account.models import OrganizationModel, BranchModel, Account
# from apps.account.models.appointments import AppointmentServiceModel
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
    payment_type = models.CharField(choices=PAYMENT_TYPE, max_length=50)
    # bank_name = models.CharField(max_length=255, null=True, blank=True)
    app_service = models.CharField(max_length=5, null=True)
    receipt = models.ForeignKey(ReceiptModel, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)
    # type = models.CharField(choices=TYPE, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, related_name="crt_transactions", on_delete=models.SET_NULL, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_transactions", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.amount} - {self.payment_type}"
