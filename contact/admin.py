from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]

    class Meta:
        model = User
admin.site.register(User, UserAdmin)
