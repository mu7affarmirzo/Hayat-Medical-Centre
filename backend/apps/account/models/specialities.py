from django.db import models

from apps.account.models import Account
from apps.account.models import OrganizationModel, BranchModel


class SpecialityModel(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_spec_by_user", on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(OrganizationModel, related_name="speciality", on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, related_name="speciality", on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.name)


class DoctorSpecialityModel(models.Model):
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_doc_spec_by_user", on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(OrganizationModel, related_name="doc_speciality", on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(BranchModel, related_name="doc_speciality", on_delete=models.SET_NULL, null=True)
    speciality = models.ForeignKey(SpecialityModel, related_name="doc_speciality", on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Account, related_name="doc_speciality", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.doctor) + " - " + str(self.speciality)



