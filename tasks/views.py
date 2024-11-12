from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Task, TaskAssignment, TaskTracking
from .forms import EmployeeForm, TaskForm, TaskAssignmentForm, TaskTrackingForm


# Example views
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee_list.html", {"employees": employees})


def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, "create_employee.html", {"form": form})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        print("the form is", form.errors)
        if form.is_valid():
            print("the form is", form)
            task = form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "create_task.html", {"form": form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})


def index(request):
    return render(request, "index.html")


import csv
from django.http import HttpResponse
from .models import TaskAssignment


def export_tasks_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="tasks.csv"'

    writer = csv.writer(response)
    writer.writerow(["Employee ID", "Employee Name", "Task Number", "Assigned Date"])

    tasks = TaskAssignment.objects.all().values_list(
        "empId__empId", "empId__empName", "taskNumber__taskNumber", "assignedDate"
    )
    for task in tasks:
        writer.writerow(task)

    return response


from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm


# Update Employee
def update_employee(request, empId):
    employee = get_object_or_404(Employee, empId=empId)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "update.html", {"form": form})


# Delete Employee
def delete_employee(request, empId):
    employee = get_object_or_404(Employee, empId=empId)
    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")
    return render(request, "delete_employee_confirm.html", {"employee": employee})


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "update_task.html", {"form": form})


# Delete Task View
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/delete_task.html", {"task": task})
