from csv import list_dialects
from django.contrib import admin
from .models import Member

# Register your models here.

@admin.register(Member)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_pw',
        'user_name',
        'user_email',
        'user_register_dttm'
    )