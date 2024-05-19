from django.db import models

from apps.account.models import BranchModel


class LabTestGroupModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self): return f"{self.name}"


class LabTestMethodModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self): return f"{self.name}"


class LabMeasurementUnitModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self): return f"{self.name} {self.unit}"


class LabWorkingStation(models.Model):
    branch = models.ForeignKey(BranchModel, related_name='lab_working_stations', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LabResearchCategoryModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class LabResearchSubCategoryModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(
        LabResearchCategoryModel, on_delete=models.SET_NULL, null=True,
        related_name='sub_categories'
    )

    def __str__(self):
        return f"{self.name}"


class LabResearchModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.BigIntegerField(default=100)
    category = models.ForeignKey(LabResearchCategoryModel, on_delete=models.SET_NULL,
                                 related_name='lab_research', null=True, blank=True)

    branch = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True)

    number = models.CharField(max_length=255, blank=True, null=True)
    alternative_code = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    attribute = models.CharField(max_length=255, blank=True, null=True)
    sub_category = models.ForeignKey(LabResearchSubCategoryModel, on_delete=models.SET_NULL,
                                     related_name='lab_research', null=True, blank=True)
    main_working_station = models.ForeignKey(
        LabWorkingStation, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='lab_main_w_s')
    backup_working_station = models.ForeignKey(
        LabWorkingStation, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='lab_backup_w_s')
    deadline = models.IntegerField(null=True, blank=True)
    deadline_cito = models.IntegerField(null=True, blank=True)
    cito = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class LabResearchTestModel(models.Model):
    RESULT_CHOICES = (
        ('строковый', 'строковый'),
        ('числовой', 'числовой'),
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    research = models.ForeignKey(LabResearchModel, on_delete=models.SET_NULL,
                                 related_name='lab_research_test', null=True, blank=True)
    group = models.ForeignKey(LabTestGroupModel, blank=True, null=True, on_delete=models.SET_NULL)
    result_type = models.CharField(max_length=255, choices=RESULT_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    ignore_status = models.BooleanField(default=False)
    is_required_print_result = models.BooleanField(default=True)
    method = models.ForeignKey(LabTestMethodModel, blank=True, null=True, on_delete=models.SET_NULL)
    instruments = models.CharField(max_length=255, blank=True, null=True)
    keyboard = models.CharField(max_length=255, blank=True, null=True)
    standard_result = models.CharField(max_length=255, null=True, blank=True)
    measurement_unit = models.ForeignKey(LabMeasurementUnitModel, on_delete=models.SET_NULL, null=True, blank=True)
    default_result = models.CharField(max_length=255, blank=True, null=True)
    additional_code = models.CharField(max_length=255, blank=True, null=True)
    additional_code_for_repeat = models.CharField(max_length=255, blank=True, null=True)
    is_micro_organism = models.BooleanField(default=False)

    id_test_system = models.CharField(max_length=255, blank=True, null=True)
    name_test_system = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
