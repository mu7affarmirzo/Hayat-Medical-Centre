from django.http import HttpResponse
from django.shortcuts import render


def main_screen_view(request):
    return render(request, 'manual/main_screen.html', {})

