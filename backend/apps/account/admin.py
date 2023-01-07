from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.account.models import (
    accounts, organizations, roles_permissions, patients, specialities, appointments, attandance
)


@admin.register(accounts.Account)
class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('email', 'username')


@admin.register(accounts.DoctorAccountModel)
class DoctorsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('doctor_email', 'doctor_l_name', 'doctor_f_name')

    def doctor_email(self, obj):
        return obj.doctor.email

    def doctor_l_name(self, obj):
        return obj.doctor.l_name

    def doctor_f_name(self, obj):
        return obj.doctor.f_name


@admin.register(organizations.OrganizationModel)
class OrganizationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


@admin.register(organizations.BranchModel)
class BranchesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


@admin.register(roles_permissions.RolesModel)
class RolesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('code', 'name', 'date_created')


@admin.register(patients.PatientGroupModel)
class PatientGroupAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


@admin.register(patients.PatientModel)
class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


@admin.register(patients.InformationSourceModel)
class InformationSourceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(appointments.MedicalService)
class MedicalServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


@admin.register(appointments.AppointmentsModel)
class AppointmentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('patient', 'doctor')


@admin.register(appointments.AppointmentServiceModel)
class AppointmentServiceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
@admin.register(appointments.EMCDocumentModel)
class EMCDocumentModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
@admin.register(accounts.ReferringDoctorModel)
class ReferringDoctorModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(roles_permissions.AccountRolesModel)
class AccountRolesModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


@admin.register(specialities.SpecialityModel)
class SpecialityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    # list_display = ('email', 'username')


@admin.register(specialities.DoctorSpecialityModel)
class DoctorSpecialityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('organization', 'branch_id', 'doctor', 'doctor_id',
                    'speciality', 'speciality_id')


@admin.register(attandance.AttendanceModel)
class AttendanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('created_at', 'staff', 'is_at_work')
