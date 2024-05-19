from apps.lis.models.lab_researchs import *
from apps.lis.models.lab_cart import *
from apps.lis.models.containers import *
from django.contrib import admin

admin.site.register(LabTestGroupModel)
admin.site.register(LabTestMethodModel)
admin.site.register(LabMeasurementUnitModel)
admin.site.register(LabWorkingStation)
admin.site.register(LabResearchCategoryModel)
admin.site.register(LabResearchSubCategoryModel)
admin.site.register(LabResearchModel)
admin.site.register(LabResearchTestModel)

admin.site.register(OrderedLabResearchModel)

admin.site.register(ContainerColorModel)
admin.site.register(ContainerGroupModel)
admin.site.register(ContainerModel)

