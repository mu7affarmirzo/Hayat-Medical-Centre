from django.db import models

from apps.account.models import DoctorAccountModel, Account
from apps.sanatorium.models import IllnessHistory


class ProcedureModel(models.Model):
    name = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    price = models.PositiveIntegerField()


class ProcedureIllnessHistoryModel(models.Model):
    STATE = (
        ("canceled", "canceled"),
        ("done", "done"),
        ("appointed", "appointed"),
        ("not come", "not come"),
    )
    illness_history = models.ForeignKey(IllnessHistory, on_delete=models.CASCADE)
    appointed_time = models.DateTimeField()
    procedure = models.ForeignKey(ProcedureModel, on_delete=models.CASCADE)
    procedure_doctor = models.ForeignKey(DoctorAccountModel, on_delete=models.CASCADE, related_name="procedure_doctor")
    state = models.CharField(max_length=255, choices=STATE, default="appointed", )

    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,
                                   related_name="appointed_doctor")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="procedure_illness_modf", on_delete=models.SET_NULL,
                                    null=True)
