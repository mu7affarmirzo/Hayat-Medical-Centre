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
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


@admin.register(organizations.BranchModel)
class BranchesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


@admin.register(roles_permissions.RolesModel)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'date_created')


admin.site.register(patients.PatientGroupModel)


@admin.register(patients.PatientModel)
class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(patients.InformationSourceModel)
admin.site.register(appointments.MedicalService)


@admin.register(appointments.AppointmentsModel)
class AppointmentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('patient', )


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
    list_display = ('organization', 'branch_id', 'doctor', 'doctor_id',
                    'speciality', 'speciality_id')


@admin.register(attandance.AttendanceModel)
class AttendanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('created_at', 'staff', 'is_at_work')
