from django.shortcuts import render
from django.views.generic import TemplateView


# ------------------------------
#           TASKS
# ------------------------------
"""
1. 

"""

# Create your views here.
class LoginViewStatic(TemplateView):
    template_name = 'warehouse/login.html'


class IndexView(TemplateView):
    template_name = 'warehouse/index.html'


class IncomeView(TemplateView):
    template_name = 'warehouse/income.html'


class MedicinesView(TemplateView):
    template_name = 'warehouse/medicines.html'
