# from django.db import models
# import datetime
# from passlib.hash import pbkdf2_sha256
# from django.utils.timezone import utc
#
#
# class OtpModel(models.Model):
#     email = models.CharField(max_length=255, null=True, blank=True)
#     otp = models.CharField(max_length=300, null=True, blank=True)
#     enc_otp = models.CharField(max_length=300, null=True, blank=True)
#     is_expired = models.SmallIntegerField(null=True, blank=True, default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     @property
#     def is_active(self):
#         now = datetime.datetime.utcnow().replace(tzinfo=utc)
#         timediff = now - self.created_at
#         timediff = timediff.total_seconds().__round__()
#         return True if timediff < 360 else False
#
#     def __str__(self):
#         return str(self.mobile)
#
#     def verify_otp(self, raw_otp):
#         return pbkdf2_sha256.verify(raw_otp, self.otp)