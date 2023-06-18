from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LoginViewStatic(TemplateView):
    template_name = 'warehouse/login.html'
