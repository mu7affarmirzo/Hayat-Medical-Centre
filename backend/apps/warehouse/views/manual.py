from django.http import HttpResponse
from django.shortcuts import render


def main_screen_view(request):
    return render(request, 'manual/main_screen.html', {})


def add_items_view(request):
    return HttpResponse('Hello World!')


def items_list_view(request):
    return HttpResponse('Hello World!')
