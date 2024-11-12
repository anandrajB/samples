from django.db import models


class Employee(models.Model):
    empId = models.AutoField(primary_key=True)
    empName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    emailId = models.EmailField()
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.empName


class Task(models.Model):
    taskNumber = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=100, default="Sample Task")
    taskDescription = models.TextField(default="No Description")
    assignedBy = models.ForeignKey(
        Employee, related_name="assigned_tasks", on_delete=models.CASCADE
    )
    assignedDate = models.DateField(auto_now_add=True)
    deadline = models.DateField()

    def __str__(self):
        return self.taskName


class TaskAssignment(models.Model):
    empId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    taskNumber = models.ForeignKey(Task, on_delete=models.CASCADE)
    assignedDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.empId.empName} - {self.taskNumber.taskName}"


class TaskTracking(models.Model):
    taskAssignment = models.ForeignKey(TaskAssignment, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.taskAssignment.taskNumber.taskName} - {self.status}"
