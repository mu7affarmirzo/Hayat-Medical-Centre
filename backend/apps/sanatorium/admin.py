from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.sanatorium.models import *


# Register your models here.
@admin.register(IllnessHistory)
class IllnessHistoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in IllnessHistory._meta.fields]


@admin.register(AmbulatoryHistory)
class AmbulatoryHistoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in AmbulatoryHistory._meta.fields]


@admin.register(ChequeModel)
class ChequeModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ChequeModel._meta.fields]


@admin.register(DiagnosisTemplate)
class DiagnosisTemplateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in DiagnosisTemplate._meta.fields]


@admin.register(ProfessionsModel)
class ProfessionsModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ProfessionsModel._meta.fields]


@admin.register(PivotPillsDrugsModel)
class PivotPillsDrugsModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in PivotPillsDrugsModel._meta.fields]


@admin.register(ToxicFactorsModel)
class ToxicFactorsModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ToxicFactorsModel._meta.fields]


@admin.register(TagsModel)
class TagsModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in TagsModel._meta.fields]


@admin.register(ScheduleModel)
class ScheduleModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ScheduleModel._meta.fields]


@admin.register(DiagnosisTemplateCategory)
class DiagnosisTemplateCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in DiagnosisTemplateCategory._meta.fields]


@admin.register(InitialAppointmentWithDoctorModel)
class InitialAppointmentWithDoctorModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in InitialAppointmentWithDoctorModel._meta.fields]


@admin.register(Consulting)
class ConsultingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in Consulting._meta.fields]


@admin.register(InitialAppointmentMedicalServiceModel)
class InitialAppointmentMedicalServiceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in InitialAppointmentMedicalServiceModel._meta.fields]


@admin.register(InitialAppointmentProcedureServiceModel)
class InitialAppointmentProcedureServiceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in InitialAppointmentProcedureServiceModel._meta.fields]


@admin.register(InitialAppointmentLabResearchServiceModel)
class InitialAppointmentLabResearchServiceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in InitialAppointmentLabResearchServiceModel._meta.fields]


@admin.register(InitialAppointmentPillsInjectionsModel)
class InitialAppointmentPillsInjectionsModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in InitialAppointmentPillsInjectionsModel._meta.fields]



@admin.register(BaseMedicalServiceModel)
class BaseMedicalServiceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in BaseMedicalServiceModel._meta.fields]


@admin.register(BaseProcedureServiceModel)
class BaseProcedureServiceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in BaseProcedureServiceModel._meta.fields]


@admin.register(BasePillsInjectionsModel)
class BasePillsInjectionsModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in BasePillsInjectionsModel._meta.fields]


@admin.register(BaseLabResearchServiceModel)
class BaseLabResearchServiceModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in BaseLabResearchServiceModel._meta.fields]




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


# MEASURED PARAMS

@admin.register(ArterialPressureModel)
class ArterialPressureAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ArterialPressureModel._meta.fields]


@admin.register(GlucometerModel)
class GlucometerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in GlucometerModel._meta.fields]


@admin.register(PulseModel)
class PulseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in PulseModel._meta.fields]


@admin.register(SaturationModel)
class SaturationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in SaturationModel._meta.fields]


@admin.register(TemperatureModel)
class TemperatureAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in TemperatureModel._meta.fields]