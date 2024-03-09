from django.contrib import admin

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
