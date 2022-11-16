from django.db import models

from apps.account.models import Account


class AttendanceModel(models.Model):
    staff = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    came_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_at_work(self):
        pass


class StaffCameToWorkModel(models.Model):
    staff = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

