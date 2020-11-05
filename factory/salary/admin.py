from django.contrib import admin
from .models import labour
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(labour)

class ViewAdmin(ImportExportModelAdmin):
    pass

