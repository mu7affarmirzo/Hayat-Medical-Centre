
import pandas as pd
from django.shortcuts import render, redirect
from apps.account.models import PatientModel


def send_excel_file(request):
    data = request.GET
    print(data)
    a = PatientModel.objects.all()
    df = pd.DataFrame(a)

    file_path = "media/data_excel/tanlangan_malumotlar.xlsx"
    df.to_excel(file_path, index=False)

    return redirect("patients_m_p")
