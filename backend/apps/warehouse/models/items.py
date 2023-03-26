from django.db import models

from apps.warehouse.models.company import CompanyModel


class ItemsModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    expire = models.DateTimeField()
    is_expired = models.BooleanField(default=False)
    expire_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.company} - {self.name} - {self.is_expired}"

    @property
    def validity_color(self):
        # 32a852 - green
        # ebeb17 - yellow
        # #171716 - black
        return 1
