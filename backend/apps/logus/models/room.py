from django.db import models
from django.db.models import Sum

from apps.account.models import Account

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
    price = models.BigIntegerField(default=0, null=True, blank=True)
    is_available = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    floor = models.IntegerField(default=1)
    view = models.CharField(max_length=200, choices=VIEW_CHOICE, default="residential")
    room_type = models.ForeignKey(RoomTypeModel, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    status_cleanest = models.CharField(choices=STATUS_CLEANEST, default="clean", max_length=30)

    room_task_type = models.CharField(choices=ROOM_TASK_TYPE, default='living', max_length=30)

    created_by = models.ForeignKey(Account, related_name="room", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_room", on_delete=models.SET_NULL, null=True)




    # @property
    # def available_capacity(self, start_date, end_date):
    #     booked_rooms = BookedRoomModel.objects.filter(
    #         room=self,
    #         end_date__gte=start_date,
    #         start_date__lte=end_date,
    #     )
    #
    #     total_booked_capacity = booked_rooms.aggregate(Sum('room__capacity'))['room__capacity__sum']
    #     total_booked_capacity = total_booked_capacity or 0  # Handle the case when there are no booked rooms
    #
    #     available_capacity = self.capacity - total_booked_capacity
    #
    #     return available_capacity if available_capacity > 0 else 0

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
