from apps.logus.models import TariffModel, RoomTypeMatrix


def get_available_rooms(tariff, room_type):
    pass


def get_type_tariff_matrix(tariff, room_type, start_date, end_date):
    tariffs = TariffModel.objects.all()
    room_types = RoomTypeMatrix.objects.all()
