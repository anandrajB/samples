from django import forms
from .models import Employee, Task, TaskAssignment, TaskTracking


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class TaskAssignmentForm(forms.ModelForm):
    class Meta:
        model = TaskAssignment
        fields = "__all__"


class TaskTrackingForm(forms.ModelForm):
    class Meta:
        model = TaskTracking
        fields = "__all__"
