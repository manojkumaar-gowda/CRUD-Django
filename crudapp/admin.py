from django.contrib import admin
from crudapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list  = ['task']

admin.site.register(Task,TaskAdmin)
