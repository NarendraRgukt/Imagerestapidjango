from django.contrib import admin
from imageapp import models
from django.contrib.auth import get_user_model


# Register your models here.
class UserProfile(admin.ModelAdmin):
    fields=("email","name","password")
admin.site.register(get_user_model(),UserProfile)  
admin.site.register(models.Image)

