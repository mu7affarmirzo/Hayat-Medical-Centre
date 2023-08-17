# from django.core.mail import send_mail
# from django.http import HttpResponse
# import pandas as pd
# from apps.account.models import PatientModel




# def send_excel_file(request):
#     data = request.GET
#     print(data)
#     a = PatientModel.objects.all()
#     df = pd.DataFrame(a)
#     df.to_excel("media/data_excel/tanlangan_malumotlar.xlsx", index=False)

#     FilePath = "media/data_excel/tanlangan_malumotlar.xlsx"

#     subject = "Excel Fayl"
#     message = "Salom, bu Excel faylni yuboraman."
#     from_email = 'your_email@gmail.com'
#     recipient_list = ['recipient@example.com']  # Yuborish kerak bo'lgan manzil

#     send_mail(subject, message, from_email, recipient_list, fail_silently=False, attachment=FilePath)
#     return HttpResponse("Excel fayl yuborildi.")

import pandas as pd
from django.shortcuts import render, redirect
from apps.account.models import PatientModel

def send_excel_file(request):
    data = request.GET
    print(data)
    a = PatientModel.objects.all()
    df = pd.DataFrame(a[0:])

    # Faylni yaratish va saqlash
    file_path = "media/data_excel/tanlangan_malumotlar.xlsx"
    df.to_excel(file_path, index=False)


    return redirect("patients_m_p")

# from django.http import JsonResponse
# from django.shortcuts import render
# import pandas as pd
# from apps.account.models import PatientModel
#
# def send_excel_file(request):
#     a = PatientModel.objects.all()
#     df = pd.DataFrame(a)
#
#     file_path = "media/data_excel/tanlangan_malumotlar.xlsx"
#     df.to_excel(file_path, index=False)
#
#     return JsonResponse({"file_path": file_path})
