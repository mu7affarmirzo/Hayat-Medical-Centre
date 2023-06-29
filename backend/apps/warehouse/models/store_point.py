from django.db import models

from apps.account.models import Account


class StorePointModel(models.Model):
    main = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_by = models.ForeignKey(Account, related_name="store", on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_store", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} - {self.address} - {self.main}"
