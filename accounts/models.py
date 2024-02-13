from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext as _

# Create your models here.
class UserManager(BaseUserManager):    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("email field cannot be empty")
        if not password:
            raise ValueError("Password field cannot be empty")
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        return user
    

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
            

class UserModel(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female",
        OTHER = "OTHER", "Other"

    username = models.CharField(max_length=25, null=False, blank=False, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, blank=False)
    password = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    is_registration_complete = models.BooleanField(default=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.OTHER)

    objects = UserManager()
    # manager = UserManager


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"
    
    def default_email(self):
        return f"{self.username}@default.com"
    
    def default_phone(self):
        return ""
    


# @receiver(pre_save,sender=User)
# def create_default_email(sender, instance:User, *args, **kwargs):
#     if not instance.email:
#         instance.email = instance.default_email()


# @receiver(pre_save, sender=User)
# def create_default_phone(sender, instance:User, *args, **kwargs):
#     if not instance.phone:
#         instance.phone = instance.default_phone