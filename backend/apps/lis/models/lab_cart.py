import uuid

from django.db import models

from apps.account.models import PatientModel, BranchModel, Account
from apps.lis.models import LabResearchModel


class OrderedLabResearchModel(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('оплачено', 'оплачено'),
        ('не оплачено', 'не оплачено'),
        ('отменена', 'отменена'),
    )
    ORDER_STATUS_CHOICES = (
        ('готово', 'готово'),
        ('в процессе', 'в процессе'),
        ('отменена', 'отменена'),
    )

    class ValidateStatus(models.TextChoices):
        green = "Невалидированные(Зеленые)"
        blue = "Валидированные(Синие)"
        black = "Неготовые(Черные)"
        all = "Все"
        not_ready = "Не готовые + Невалидированные"
        unnorm = "Вне нормы"
        expired = "Просроченные по постановке"
        expired2 = "Просроченные по готовности"
        expired3 = "Просроченные по валидации"
        with_results = "Не готовые, но с результатами"

    order_number = models.CharField(max_length=255, default=uuid.uuid4, editable=False)
    container_id = models.CharField(max_length=255, null=True, blank=True)

    patient = models.ForeignKey(PatientModel, on_delete=models.SET_NULL, null=True, blank=True)
    lab_code = models.CharField(max_length=255, null=True, blank=True)
    lab = models.ForeignKey(LabResearchModel, models.SET_NULL, null=True, blank=True, related_name='cart_lab_research')
    cito = models.BooleanField(default=False)
    branch_name = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True, blank=True)
    staging = models.CharField(max_length=255, null=True, blank=True)
    delivery_point = models.ForeignKey(BranchModel, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='lab_delivery_point')
    validate_status = models.CharField(choices=ValidateStatus.choices, null=True, blank=True, max_length=50)
    delivery_date = models.DateTimeField(null=True, blank=True)
    queue_number = models.CharField(max_length=255, null=True, blank=True)
    lab_assistant_comment = models.TextField(null=True, blank=True)
    expected_date = models.CharField(max_length=255, null=True, blank=True)
    pathology = models.BooleanField(default=True)

    payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, max_length=255, null=True, blank=True)
    order_status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=255, default='в процессе')

    validated_by = models.ForeignKey(Account, related_name="validated_cart_lab_research", on_delete=models.SET_NULL,
                                     null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name='registered_by')

    modified_by = models.ForeignKey(Account, related_name="modf_cart_lab_research", on_delete=models.SET_NULL,
                                    null=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order_number}'

    class Meta:
        ordering = ('-created_at',)


class TestResultModel(models.Model):
    STATUS_CHOICES = (
        ('выше нормы', 'выше нормы'),
        ('в норме', 'в норме'),
        ('отменена', 'отменена'),
    )
    TEST_STATUS_CHOICES = (
        ('готово', 'готово'),
        ('в процессе', 'в процессе'),
        ('отменена', 'отменена'),
    )
    ordered_lab_research = models.ForeignKey(OrderedLabResearchModel, on_delete=models.CASCADE,
                                             related_name='test_results')
    lab_research_test = models.ForeignKey('LabResearchTestModel', on_delete=models.CASCADE)
    container = models.ForeignKey('ContainerModel', on_delete=models.CASCADE)
    container_code = models.CharField(null=True, blank=True, max_length=255)
    result = models.TextField()
    result_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, null=True, blank=True, max_length=255)
    test_status = models.CharField(choices=TEST_STATUS_CHOICES, max_length=255, default='в процессе')

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name='registered_by')

    modified_by = models.ForeignKey(Account, related_name="modf_cart_lab_test", on_delete=models.SET_NULL,
                                    null=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.lab_research_test.name} - {self.ordered_lab_research.order_number}"

# class LogTestResultModel(models.Model):
#     STATUS_CHOICES = (
#         ('выше нормы', 'выше нормы'),
#         ('в норме', 'в норме'),
#         ('отменена', 'отменена'),
#     )
#     TEST_STATUS_CHOICES = (
#         ('готово', 'готово'),
#         ('в процессе', 'в процессе'),
#         ('отменена', 'отменена'),
#     )
#     test_result = models.ForeignKey(TestResultModel, on_delete=models.CASCADE)
#     ordered_lab_research = models.ForeignKey(OrderedLabResearchModel, on_delete=models.CASCADE,
#                                              related_name='test_results')
#     lab_research_test = models.ForeignKey('LabResearchTestModel', on_delete=models.CASCADE)
#     container = models.ForeignKey('ContainerModel', on_delete=models.CASCADE)
#     container_code = models.CharField(null=True, blank=True, max_length=255)
#     result = models.TextField()
#     result_date = models.DateTimeField(null=True, blank=True)
#     status = models.CharField(choices=STATUS_CHOICES, null=True, blank=True, max_length=255)
#     test_status = models.CharField(choices=TEST_STATUS_CHOICES, max_length=255, default='в процессе')
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name='registered_by')
#
#     modified_by = models.ForeignKey(Account, related_name="modf_cart_lab_test", on_delete=models.SET_NULL,
#                                     null=True)
#     modified_at = models.DateTimeField(auto_now_add=True)
#
#
# @receiver(pre_save, sender=TestResultModel)
# def test_results_log_view(sender, instance: TestResultModel = None, created=False, **kwargs):
#     if instance.id:
#         LogTestResultModel(test_result=instance, )
#         pass
