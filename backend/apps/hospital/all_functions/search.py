from rest_framework.response import Response
from django.db.models import Q
from django.shortcuts import render, HttpResponse

from apps.account.models import PatientModel
from apps.logus.models import BookedRoomModel
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def patients_m_p_search(requests):
    data = requests.POST['inputValue']
    # p = PatientModel.objects.get(f_name=data)
    # patient_search = BookedRoomModel.objects.get(patients=p)
    p = PatientModel.objects.filter(Q(f_name=data) | Q(l_name=data) | Q(mid_name=data)).first()
    room_model = BookedRoomModel.objects.filter(patients=p)
    # return render(requests, 'Hospital/patients-my-patients.html',
    #               {"room": room_model, "room_len": len(room_model), "today": a.year})

    # return Response({"room": room_model, "room_len": len(room_model), "today": a.year})
    # return Response(x.room_patents for x in room_model)
    return Response({
        "result": [i.room_patents() for i in room_model]
    }, template_name='Hospital/patients-my-patients.html')
    # patients = PatientModel.objects.all().order_by('id')
