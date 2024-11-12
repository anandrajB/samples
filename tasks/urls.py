from django.urls import path, include
from . import views
from .employee_urls import urlpatterns as employee_urls
from .task_urls import urlpatterns as task_urls

urlpatterns = [
    path("employee/", include(employee_urls)),
    path("task/", include(task_urls)),
]
