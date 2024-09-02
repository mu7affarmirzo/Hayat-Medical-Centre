from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.account.models import (
    accounts, organizations, roles_permissions, patients, specialities, appointments, attandance,
notifications
)


@admin.register(notifications.NotificationModel)
class NotificationModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in notifications.NotificationModel._meta.fields]


@admin.register(accounts.Account)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in accounts.Account._meta.fields]


@admin.register(accounts.NurseAccountModel)
class NurseAccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in accounts.NurseAccountModel._meta.fields]


@admin.register(accounts.DoctorAccountModel)
class DoctorsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in accounts.DoctorAccountModel._meta.fields]

    def doctor_email(self, obj):
        return obj.doctor.email

    def doctor_l_name(self, obj):
        return obj.doctor.l_name

    def doctor_f_name(self, obj):
        return obj.doctor.f_name


@admin.register(organizations.OrganizationModel)
class OrganizationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in organizations.OrganizationModel._meta.fields]


@admin.register(organizations.BranchModel)
class BranchesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in organizations.BranchModel._meta.fields]


@admin.register(roles_permissions.RolesModel)
class RolesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in roles_permissions.RolesModel._meta.fields]


@admin.register(patients.PatientGroupModel)
class PatientGroupAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in patients.PatientGroupModel._meta.fields]


@admin.register(patients.PatientModel)
class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in patients.PatientModel._meta.fields]


@admin.register(patients.InformationSourceModel)
class InformationSourceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in patients.InformationSourceModel._meta.fields]


@admin.register(appointments.MedicalService)
class MedicalServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in appointments.MedicalService._meta.fields]


@admin.register(appointments.AppointmentsModel)
class AppointmentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in appointments.AppointmentsModel._meta.fields]


@admin.register(appointments.AppointmentServiceModel)
class AppointmentServiceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in appointments.AppointmentServiceModel._meta.fields]


@admin.register(appointments.EMCDocumentModel)
class EMCDocumentModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in appointments.EMCDocumentModel._meta.fields]


@admin.register(accounts.ReferringDoctorModel)
class ReferringDoctorModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in accounts.ReferringDoctorModel._meta.fields]


@admin.register(roles_permissions.AccountRolesModel)
class AccountRolesModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in roles_permissions.AccountRolesModel._meta.fields]


@admin.register(specialities.SpecialityModel)
class SpecialityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in specialities.SpecialityModel._meta.fields]


@admin.register(specialities.DoctorSpecialityModel)
class DoctorSpecialityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = [field.name for field in specialities.DoctorSpecialityModel._meta.fields]


@admin.register(attandance.AttendanceModel)
class AttendanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in attandance.AttendanceModel._meta.fields]

