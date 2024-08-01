from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from apps.logus.models import BookingModel


@login_required(login_url="logus_auth:login")
def get_upcoming_checkouts(request):
    context = {}

    checkouts = BookingModel.objects.filter(end_date=timezone.now().date())
    context['bookings'] = checkouts

    return render(request, 'logus/checkouts.html', context)



