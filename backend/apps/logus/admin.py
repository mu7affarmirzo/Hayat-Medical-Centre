from django.contrib import admin
from apps.logus.models import *

# Register your models here.
admin.site.register(RoomModel)
admin.site.register(BookedRoomModel)
admin.site.register(TariffModel)
admin.site.register(RoomTypeModel)
admin.site.register(BookingModel)
admin.site.register(RoomTariffModel)
admin.site.register(ServiceModel)
admin.site.register(TariffServiceModel)
