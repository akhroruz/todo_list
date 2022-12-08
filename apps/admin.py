from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Task


@admin.register(Task)
class TaskAdmin(ModelAdmin):
    pass
