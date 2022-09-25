from django.db import models

from account.models.accounts import Account
from account.models.organizations import OrganizationModel


class InformationSourceModel(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_info_src", on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(OrganizationModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


class PatientGroupModel(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    exemption_percentage = models.IntegerField(default=1)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_patient_gr", on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(OrganizationModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


class PatientModel(models.Model):
    f_name = models.CharField(max_length=255)
    mid_name = models.CharField(max_length=255, null=True, blank=True)
    l_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    home_phone_number = models.CharField(max_length=255, blank=True, null=True)
    mobile_phone_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    additional_info = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    information_source = models.OneToOneField(InformationSourceModel, on_delete=models.CASCADE)
    patient_group = models.ManyToManyField(PatientGroupModel)
    doc_type = models.CharField(max_length=255, blank=True, null=True)
    doc_number = models.CharField(max_length=255, blank=True, null=True)
    issued_data = models.DateField(auto_now=True)
    INN = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_patient_by_user", on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(OrganizationModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):

        try:
            mid_name = self.mid_name
        except:
            mid_name = ''

        return f"{self.f_name} {self.l_name} {mid_name}"

    class Meta:
        ordering = ('f_name', '-created_at')

