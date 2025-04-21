from http.client import HTTPResponse

from django.contrib.auth import authenticate, logout, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect

from apps.decorators import role_required
from apps.massage.models import PaymentModel, SessionModel


BOOKINGS_PER_PAGE = 30


def paginate_page(request, queries):
    page = request.GET.get('page', 1)
    sessions_paginator = Paginator(queries, BOOKINGS_PER_PAGE)

    try:
        sessions = sessions_paginator.page(page)
    except PageNotAnInteger:
        sessions = sessions_paginator.page(BOOKINGS_PER_PAGE)
    except EmptyPage:
        sessions = sessions_paginator.page(sessions_paginator.num_pages)
    return sessions


def logout_view(request):
    logout(request)
    return redirect('login')


@role_required(role='massage.reception', login_url='massage_reception:logout')
def main_screen_view(request):

    sessions = SessionModel.objects.all()
    sessions = paginate_page(request, sessions)

    context = {'sessions': sessions}
    return render(request, 'reception/main_screen.html', context)


def not_paid_list_view(request):

    sessions = SessionModel.objects.filter(is_paid=False)
    sessions = paginate_page(request, sessions)

    context = {'sessions': sessions}
    return render(request, 'reception/main_screen.html', context)


def get_booking_queryset(query=None, stage=None):
    queryset = []
    queries = query.split(" ")

    for q in queries:
        if stage:
            sessions = (SessionModel.objects.filter(
                Q(series__icontains=q) |
                Q(patient__f_name__icontains=q) |
                Q(patient__mid_name__icontains=q) |
                Q(patient__mobile_phone_number__icontains=q)
            ).distinct())
        else:
            sessions = (SessionModel.objects.filter(
                Q(series__icontains=q) |
                Q(patient__f_name__icontains=q) |
                Q(patient__mid_name__icontains=q) |
                Q(patient__mobile_phone_number__icontains=q)
            ).distinct())
        for new in sessions:
            queryset.append(new)

    return list(set(queryset))