from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_list, name="employee_list"),
    path("create/", views.create_employee, name="create_employee"),
    path("update/<int:empId>/", views.update_employee, name="update_employee"),
    path("delete/<int:empId>/", views.delete_employee, name="delete_employee"),
]
