from django.db import models

from account.models import Account


class RolesModel(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class AccountRolesModel(models.Model):
    role = models.ForeignKey(RolesModel, related_name='account_role_role', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name='account_role_user', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.role) + "-" + str(self.user)


class PermissionsModel(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class RolePermissionModel(models.Model):
    permission = models.ForeignKey(PermissionsModel, related_name='role_permission_perm', on_delete=models.CASCADE)
    role = models.ForeignKey(RolesModel, related_name='role_permission_role', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.role) + "-" + str(self.permission)
