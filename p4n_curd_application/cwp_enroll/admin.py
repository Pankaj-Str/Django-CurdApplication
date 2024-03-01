from django.contrib import admin

# Register your models here.

from .models import *   
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
    