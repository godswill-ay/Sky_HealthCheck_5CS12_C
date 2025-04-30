##Zaamin Qadeer w1906890
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Department, Team, Session, Card, Vote

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

admin.site.register(Department)
admin.site.register(Team)
admin.site.register(Session)
admin.site.register(Card)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'card', 'vote', 'progress_better')
    list_filter  = ('vote', 'session', 'card')
