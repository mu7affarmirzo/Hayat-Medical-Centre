from django.db import models

from apps.account.models import Account

VIEW_CHOICE = (
    ("residential", "residential"),
    ("mountains", "mountains"),
    ("river", "river"),
)


class TariffModel(models.Model):
    color = models.CharField(null=True, blank=True, max_length=20)
    tag = models.CharField(null=True, blank=True, max_length=20)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(Account, related_name="tariff", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_tariff", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class RoomTypeModel(models.Model):
    name = models.CharField(max_length=255)
    # tariff = models.ForeignKey(TariffModel, on_delete=models.CASCADE)
    tag = models.CharField(null=True, blank=True, max_length=20)
    color = models.CharField(null=True, blank=True, max_length=20)
    created_by = models.ForeignKey(Account, related_name="type", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_type", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class RoomModel(models.Model):
    room_number = models.CharField(max_length=50)
    is_available = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    floor = models.IntegerField(default=1)
    view = models.CharField(max_length=200, choices=VIEW_CHOICE, default="residential")
    room_type = models.ForeignKey(RoomTypeModel, on_delete=models.CASCADE)
    capacity = models.IntegerField()

    created_by = models.ForeignKey(Account, related_name="room", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_room", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.room_number} - {self.is_available} - {self.room_type} - {self.capacity}"


class RoomPrice(models.Model):
    tariff = models.ForeignKey(TariffModel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomTypeModel, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    price = models.BigIntegerField()

    created_by = models.ForeignKey(Account, related_name="room_price", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_room_price", on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ['tariff', 'room_type', 'room']

    def __str__(self):
        return f"{self.room.room_number} - {self.tariff.name} - {self.room_type.name} - {self.price}"


class TariffXTypeModel(models.Model):
    tariff = models.ForeignKey(TariffModel, on_delete=models.CASCADE)
    type = models.ForeignKey(RoomTypeModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tariff.name} - {self.type.name}"
