from django.db import models

from account.models import Account


class OrganizationModel(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_org_by_user", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


class BranchModel(models.Model):
    organization = models.ForeignKey(OrganizationModel, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_branch_by_user", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        try:
            org_name = self.organization
        except:
            org_name = ""
        return str(self.name) + " - " + str(org_name)
