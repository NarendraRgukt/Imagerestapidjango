from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth import get_user_model

class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("Please provide your email id")
        email=self.normalize_email(email)
        user=self.model(name=name,email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.is_active=True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=50,unique=True,blank=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    objects=UserProfileManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]
    

    def get_full_name(self):
        return self.name
    def __str__(self):
        return self.email
    




class Image(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    image=models.ImageField(upload_to="media")
    

    def __str__(self):
        return f"{self.user.name} image"



