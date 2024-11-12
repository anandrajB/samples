from django.contrib import admin
from .models import Employee, Task, TaskAssignment, TaskTracking

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(TaskAssignment)
admin.site.register(TaskTracking)
