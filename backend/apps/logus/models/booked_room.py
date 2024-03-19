from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.account.models import Account, PatientModel
from apps.logus.models import RoomModel, RoomTypeModel, TariffModel, LogusChequeModel

DISCOUNT_CHOICES = (
    (0, 0),
    (5, 5),
    (10, 10),
    (15, 15),
    (20, 20),
    (25, 25),
    (30, 30),
)
SEGMENT = (
    ("ОСН", "Основной")
)
STAGES = (
    ('booked', 'booked'),
    ('settled', 'settled'),
    ('arrived', 'arrived'),
    ('cancelled', 'cancelled'),
)


class BookedRoomModel(models.Model):
    tariff = models.ForeignKey(TariffModel, on_delete=models.SET_NULL, null=True,
                               related_name='booked_room_tariff', blank=True)
    room = models.ForeignKey('RoomModel', on_delete=models.SET_NULL, null=True)
    room_type = models.ForeignKey(RoomTypeModel, on_delete=models.SET_NULL, null=True)
    patients = models.ForeignKey(PatientModel, on_delete=models.SET_NULL, null=True, related_name="booked_rooms")
    discount = models.IntegerField(choices=DISCOUNT_CHOICES, null=True, blank=True, default=0)
    cheque = models.OneToOneField(LogusChequeModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_checked_out = models.BooleanField(default=False)
    stage = models.CharField(choices=STAGES, max_length=10, default='booked')

    start_date = models.DateField()
    end_date = models.DateField()
    # marketing
    # segment = models.CharField(choices=)

    created_by = models.ForeignKey(Account, related_name="booked_room", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_booked_room", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.room} - {self.patients}"  # - {self.room_price.tariff}"

    @property
    def duration(self):
        if self.start_date and self.end_date:

            duration = self.end_date - self.start_date
            return duration.days
        else:
            return None


class BookedRoomTariffsModel(models.Model):
    booked_room = models.ForeignKey(BookedRoomModel, on_delete=models.SET_NULL, null=True)
    tariff = models.ForeignKey(TariffModel, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(default=0)
    is_paid = models.BooleanField(default=False)

    start_date = models.DateField()
    end_date = models.DateField()

    created_by = models.ForeignKey(Account, related_name="bk_rm_tariff", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="mdf_bk_rm_tariff", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.booked_room}-{self.tariff}"


class BookedRoomRoomModel(models.Model):
    booked_room = models.ForeignKey(BookedRoomModel, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(RoomModel, on_delete=models.SET_NULL, null=True)
    room_type = models.ForeignKey(RoomTypeModel, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(default=0)
    is_paid = models.BooleanField(default=False)

    start_date = models.DateField()
    end_date = models.DateField()

    created_by = models.ForeignKey(Account, related_name="bk_rm_room", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="mdf_bk_rm_room", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.booked_room}-{self.room}-{self.room_type}"


@receiver(post_save, sender=BookedRoomModel)
def cheque_create_add(sender, instance: BookedRoomModel = None, created=False, **kwargs):
    if created:
        # TODO optimize
        booked_room_tariff = BookedRoomTariffsModel.objects.create(booked_room=instance, tariff=instance.tariff,
                                                                   price=instance.tariff.price,
                                                                   start_date=instance.start_date,
                                                                   end_date=instance.end_date,
                                                                   created_by=instance.created_by,
                                                                   modified_by=instance.modified_by)
        booked_room_type = BookedRoomRoomModel.objects.create(booked_room=instance, room=instance.room,
                                                              room_type=instance.room_type,
                                                              price=instance.room.price,
                                                              start_date=instance.start_date,
                                                              end_date=instance.end_date,
                                                              created_by=instance.created_by,
                                                              modified_by=instance.modified_by)
        cheque = LogusChequeModel.objects.create(
            patient=instance.patients,
            created_by=instance.created_by,
            modified_by=instance.modified_by
        )
        instance.cheque = cheque
        instance.save(update_fields=["cheque"])
    elif instance.cheque is None:
        cheque = LogusChequeModel.objects.create(
            patient=instance.patients,
            created_by=instance.created_by,
            modified_by=instance.modified_by
        )
        instance.cheque = cheque
        instance.save(update_fields=["cheque"])
