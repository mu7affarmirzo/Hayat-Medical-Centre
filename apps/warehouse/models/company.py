from django.db import models

from apps.account.models import Account


class CompanyModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name='company')
    modified_by = models.ForeignKey(Account, related_name="modf_company", on_delete=models.SET_NULL, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

