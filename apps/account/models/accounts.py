from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have email")
        if not username:
            raise ValueError("Users must have username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    f_name = models.CharField(max_length=50, null=True)
    l_name = models.CharField(max_length=50, null=True)
    m_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=30, null=True)
    tg_username = models.CharField(max_length=255, null=True, blank=True)
    sex = models.BooleanField(default=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    organization_id = models.IntegerField(null=True)
    branch_id = models.IntegerField(null=True)
    color = models.CharField(max_length=255, null=True)
    is_admin = models.BooleanField(default=False)
    is_therapist = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    @property
    def full_name(self):
        try:
            m_name = self.m_name
        except:
            m_name = ''

        return f"{self.f_name} {self.l_name} {m_name}"

    @property
    def unread_notifications(self):
        return self.notifications.filter(state=False)


class DoctorSpecialtyTypeModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class DoctorAccountModel(models.Model):
    specialty_type = models.ForeignKey('DoctorSpecialtyTypeModel', on_delete=models.SET_NULL, null=True)
    doctor = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='doctor_model')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.doctor.full_name)


class NurseAccountModel(models.Model):
    nurse = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='nurse_model')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nurse.full_name)


class ReferringDoctorModel(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Account, related_name="modf_ref_doc_by_user", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)
