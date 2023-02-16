from django.db import models

from apps.warehouse.models.company import CompanyModel


class ItemsModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    expire = models.DateTimeField()
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company} - {self.name} - {self.is_expired}"