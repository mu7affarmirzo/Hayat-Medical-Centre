from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.account.models import (
    accounts, organizations, roles_permissions, patients, specialities
)
from apps.account.models import appointments


@admin.register(accounts.Account)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('email', 'username')


@admin.register(organizations.OrganizationModel)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


@admin.register(organizations.BranchModel)
class BranchesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


@admin.register(roles_permissions.RolesModel)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'date_created')


admin.site.register(patients.PatientGroupModel)
admin.site.register(patients.PatientModel)
admin.site.register(patients.InformationSourceModel)
admin.site.register(appointments.MedicalService)
admin.site.register(appointments.AppointmentsModel)
admin.site.register(appointments.AppointmentServiceModel)
admin.site.register(appointments.EMCDocumentModel)
admin.site.register(accounts.ReferringDoctorModel)
admin.site.register(roles_permissions.AccountRolesModel)


@admin.register(specialities.SpecialityModel)
class SpecialityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    # list_display = ('email', 'username')


@admin.register(specialities.DoctorSpecialityModel)
class DoctorSpecialityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    # list_display = ('email', 'username')