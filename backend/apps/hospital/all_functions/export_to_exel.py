import pandas as pd
from django.shortcuts import render, redirect
from apps.logus.models import BookedRoomModel


def send_excel_file(request):
    a = BookedRoomModel.objects.all()
    df = pd.DataFrame(a)

    file_path = "media/data_excel/tanlangan_malumotlar.xlsx"
    df.to_excel(file_path, index=False)

    return redirect("patients_m_p")
