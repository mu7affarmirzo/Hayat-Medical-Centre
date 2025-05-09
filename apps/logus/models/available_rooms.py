from django.db import models

from apps.account.models import Account, MedicalService

VIEW_CHOICE = (
    ("residential", "residential"),
    ("mountains", "mountains"),
    ("river", "river"),
)

STATUS_CLEANEST = (
    ("clean", "clean"),
    ("dirty", "dirty")
)


ROOM_TASK_TYPE = (
    ("living", "living"),
    ("service", "service"),
    ("security", "security"),
)


class AvailableTariffModel(models.Model):
    color = models.CharField(null=True, blank=True, max_length=20)
    tag = models.CharField(null=True, blank=True, max_length=20)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)

    medical_service = models.ManyToManyField(MedicalService)

    created_by = models.ForeignKey(Account, related_name="available_tariff", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_available_tariff", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class AvailableRoomsTypeModel(models.Model):
    name = models.CharField(max_length=255)
    tag = models.CharField(null=True, blank=True, max_length=20)
    color = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        return f"{self.name}"


class AvailableRoomModel(models.Model):
    room_number = models.CharField(max_length=50)
    is_available = models.BooleanField(default=False)
    floor = models.IntegerField(default=1)
    view = models.CharField(max_length=200, choices=VIEW_CHOICE, default="residential")
    capacity = models.IntegerField()
    status_cleanest = models.CharField(choices=STATUS_CLEANEST, default="clean", max_length=30)

    room_task_type = models.CharField(choices=ROOM_TASK_TYPE, default='living', max_length=30)

    def __str__(self):
        return f"{self.room_number} - {self.is_available}"


class RoomTypeMatrix(models.Model):
    room = models.ForeignKey(AvailableRoomModel, on_delete=models.CASCADE, related_name="available_room")
    room_type = models.ForeignKey(AvailableRoomsTypeModel, on_delete=models.CASCADE, related_name="room_type")
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.room}| {self.room_type} | - {self.price}"


class TariffRoomTypeMatrixModel(models.Model):
    tariff = models.ForeignKey(AvailableTariffModel, on_delete=models.CASCADE, related_name="matrix", null=True, blank=True)
    room_type = models.ForeignKey(AvailableRoomsTypeModel, on_delete=models.CASCADE,  related_name="matrix", null=True, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.tariff}"
