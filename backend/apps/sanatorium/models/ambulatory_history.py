import uuid

from django.db import models

from apps.account.models import Account
from apps.account.models import PatientModel
from apps.logus.models import BookedRoomModel


class AmbulatoryHistory(models.Model):
    series_number = models.CharField(max_length=255, default=uuid.uuid4)
    diagnosis = models.CharField(max_length=511)
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE, related_name="ambulatory_histories")
    doctor = models.ForeignKey(Account, on_delete=models.CASCADE)
    # nurse = models.ForeignKey(Account, on_delete=models.CASCADE)
    booking = models.ForeignKey(BookedRoomModel, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="ambulatory_histories")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_ambulatory_by_user", on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ["patient", "booking"]

    def __str__(self):
        return self.patient.f_name
