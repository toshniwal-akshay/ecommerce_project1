from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUseAdmin

from .models import *

User = get_user_model()


class UserAdmin(BaseUseAdmin):

    list_display = ('id', 'name', 'email')
    list_ordering = ['-id']
    list_filter = ('shop', 'active')
    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'email', 'address', 'dob', 'gender','shop_name')}),
        ('Permissions', {
            'fields': ('active','is_verified','shop', 'admin')}),
    )

    search_fields = ('email', 'name')
    ordering = ('email', 'name', 'id')
    filter_horizontal = ()


# Register your models here.
admin.site.register(User, UserAdmin)
