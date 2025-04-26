from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Department, Team, CustomUser

admin.site.register(Department)
admin.site.register(Team)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role', 'team')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Info', {'fields': ('role', 'team')}),
    )
