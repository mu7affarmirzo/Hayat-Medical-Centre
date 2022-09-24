from django.contrib import admin
from account.models import account, organization, roles_permission


@admin.register(account.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username')


@admin.register(organization.OrganizationModel)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


@admin.register(organization.BranchModel)
class BranchesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


@admin.register(roles_permission.RolesModel)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'date_created')
