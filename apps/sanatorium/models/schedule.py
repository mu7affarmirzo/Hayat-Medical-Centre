from django.db import models
from apps.account.models import PatientModel, Account
from apps.logus.models import ServiceModel, RoomModel
from apps.sanatorium.models import IllnessHistory

STATUS_CHOICES = (
    ("done", "done"),
    ("assigned", "assigned"),
    ("cancel", "cancel"),
    ("didn't come", "didn't come")
)


class ScheduleModel(models.Model):
    illness_history = models.ForeignKey(IllnessHistory, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    procedure_doctor = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="doctor_procedures")
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name='service_schedule_room', null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=255, default="assigned")
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="schedules")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_schedule_by_user", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.status






















