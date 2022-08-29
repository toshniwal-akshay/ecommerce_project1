"Custom Import"
from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class ManageUsers(BaseUserManager):
    "Base User Model"

    def create_user(self, email, password=None, is_staff=False, is_active=True, admin=False):
        "Overriding Create User Method of Base User Model"

        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('User must have an Password')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.shop = is_staff
        user.active = is_active
        user.admin = admin

        user.save(using=self._db)

        return user

    def create_staffuser(self, email, password=None):
        "Created Staff Method of Base User Model"
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        "Overriding Create SuperUser Method of Base User Model"

        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            admin=True,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    "Custom Model  Extended from Base User Model"
    MALE =1
    FEMALE = 2
    OTHER = 3

    GENDER_CHOICE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),

    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=500)
    password = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    shop = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    shop_name = models.CharField(max_length=100 , blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICE, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ManageUsers()

    def __str__(self):
        return str(self.email)

    def get_name(self):
        "Return Name of User"
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of shop?"
        return self.shop

    @property
    def is_active(self):
        "Is the user a member active?"
        return self.active

    @property
    def is_superuser(self):
        "Is the user admin?"
        return self.admin
