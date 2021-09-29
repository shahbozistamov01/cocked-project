from django.contrib import admin
from .models import bootstrap_user
# Register your models here.

class bootstrap_user_admin(admin.ModelAdmin):
    list_display = ['name','discription']

admin.site.register(bootstrap_user,bootstrap_user_admin)
