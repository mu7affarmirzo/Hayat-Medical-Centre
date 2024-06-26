from django.db import models
from apps.account.models import Account


class StorePointRolesModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class StorePointModel(models.Model):
    is_main = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_by = models.ForeignKey(Account, related_name="store", on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_store", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} - {self.address} - {self.is_main}"


# class StorePointStaffModel(models.Model):
#     staff = models.OneToOneField(Account, related_name="store_staff", on_delete=models.SET_NULL, null=True, blank=True)
#     store_point = models.ForeignKey(StorePointModel, related_name="store_point_staff", on_delete=models.SET_NULL, null=True, blank=True)
#     role = models.ForeignKey(StorePointRolesModel, related_name="store_point_role", on_delete=models.SET_NULL, null=True, blank=True)
#
#     def __str__(self):
#         return f"{self.store_point} - {self.role}"
#
#     class Meta:
#         unique_together = ('staff', 'store_point')

class StorePointStaffModel(models.Model):
    staff = models.ForeignKey(Account, related_name="store_staff", on_delete=models.SET_NULL, null=True, blank=True)
    store_point = models.ForeignKey(StorePointModel, related_name="store_point_staff", on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(StorePointRolesModel, related_name="store_point_role", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.store_point} - {self.role}"

    class Meta:
        unique_together = ('staff', 'store_point')
