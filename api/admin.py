from django.contrib import admin
from api.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display: "__all__"
