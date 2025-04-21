from import_export.admin import ImportExportModelAdmin

from apps.lis.models.lab_researchs import *
from apps.lis.models.lab_cart import *
from apps.lis.models.containers import *
from django.contrib import admin


@admin.register(LabTestGroupModel)
class LabTestGroupModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in LabTestGroupModel._meta.fields]


@admin.register(LabTestMethodModel)
class LabTestMethodModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in LabTestMethodModel._meta.fields]


@admin.register(LabMeasurementUnitModel)
class LabMeasurementUnitModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in LabMeasurementUnitModel._meta.fields]


@admin.register(LabWorkingStation)
class LabWorkingStationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in LabWorkingStation._meta.fields]


@admin.register(LabResearchCategoryModel)
class LabResearchCategoryModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in LabResearchCategoryModel._meta.fields]


@admin.register(LabResearchSubCategoryModel)
class LabResearchSubCategoryModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in LabResearchSubCategoryModel._meta.fields]


@admin.register(LabResearchModel)
class LabResearchModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in LabResearchModel._meta.fields]


@admin.register(LabResearchTestModel)
class LabResearchTestModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in LabResearchTestModel._meta.fields]



@admin.register(OrderedLabResearchModel)
class OrderedLabResearchModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in OrderedLabResearchModel._meta.fields]



@admin.register(ContainerColorModel)
class ContainerColorModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ContainerColorModel._meta.fields]


@admin.register(ContainerGroupModel)
class ContainerGroupModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ContainerGroupModel._meta.fields]


@admin.register(ContainerModel)
class ContainerModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in ContainerModel._meta.fields]


@admin.register(TestResultModel)
class TestResultModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [field.name for field in TestResultModel._meta.fields]



