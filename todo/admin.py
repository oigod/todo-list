from django.contrib import admin

from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_display = ("content", "datetime", "deadline", "is_done")
    list_filter = ("is_done",)
