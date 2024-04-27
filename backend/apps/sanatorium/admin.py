from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.sanatorium.models import *

# Register your models here.
admin.site.register(IllnessHistory)
admin.site.register(AmbulatoryHistory)
admin.site.register(ChequeModel)
admin.site.register(DiagnosisTemplate)
admin.site.register(ProfessionsModel)
admin.site.register(PivotPillsDrugsModel)
admin.site.register(ToxicFactorsModel)
admin.site.register(TagsModel)
admin.site.register(ScheduleModel)
admin.site.register(DiagnosisTemplateCategory)
admin.site.register(InitialAppointmentWithDoctorModel)
admin.site.register(Consulting)
admin.site.register(InitialAppointmentMedicalServiceModel)
admin.site.register(InitialAppointmentProcedureServiceModel)
admin.site.register(InitialAppointmentLabResearchServiceModel)
admin.site.register(InitialAppointmentPillsInjectionsModel)

admin.site.register(BaseMedicalServiceModel)
admin.site.register(BaseProcedureServiceModel)
admin.site.register(BasePillsInjectionsModel)
admin.site.register(BaseLabResearchServiceModel)


@admin.register(BasicTemplateModel)
class BasicTemplateModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


@admin.register(ConsultingWithNeurologistModel)
class ConsultingWithNeurologistAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ConsultingWithNeurologistModel._meta.fields]


@admin.register(ConsultingWithCardiologistModel)
class ConsultingWithCardiologistAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ConsultingWithCardiologistModel._meta.fields]


@admin.register(AppointmentWithOnDutyDoctorModel)
class AppointmentWithOnDutyDoctorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in AppointmentWithOnDutyDoctorModel._meta.fields]


@admin.register(AppointmentWithOnDutyDoctorOnArrivalModel)
class AppointmentWithOnDutyDoctorOnArrivalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in AppointmentWithOnDutyDoctorOnArrivalModel._meta.fields]


@admin.register(RepeatedAppointmentWithDoctorModel)
class RepeatedAppointmentWithDoctorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in RepeatedAppointmentWithDoctorModel._meta.fields]


@admin.register(FinalAppointmentWithDoctorModel)
class FinalAppointmentWithDoctorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in FinalAppointmentWithDoctorModel._meta.fields]


@admin.register(EkgAppointmentModel)
class EkgAppointmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in EkgAppointmentModel._meta.fields]



