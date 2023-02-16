from django.db import models


class CompanyModel(models.Model):
    name = models.CharField(max_length=255)


