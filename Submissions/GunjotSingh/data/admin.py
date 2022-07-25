from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
from .models import userData

class userDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(userData,userDataAdmin)