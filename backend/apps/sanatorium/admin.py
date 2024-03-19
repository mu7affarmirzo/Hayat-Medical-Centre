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


@admin.register(BasicTemplateModel)
class BasicTemplateModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
