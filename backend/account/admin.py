from django.contrib import admin
from account.models import (
    accounts, organizations, roles_permissions, patients, appointments, specialities
)


@admin.register(accounts.Account)
class AccountAdmin(admin.ModelAdmin):
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
