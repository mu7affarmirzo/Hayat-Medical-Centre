from django.db import models

from apps.account.models import BranchModel


class LabResearchCategoryModel(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class LabResearchModel(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.BigIntegerField(default=100)
    category = models.ForeignKey(LabResearchCategoryModel, on_delete=models.SET_NULL,
                                 related_name='lab_research', null=True, blank=True)

    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


