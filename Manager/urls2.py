from django.urls import path
from . import views
urlpatterns = [
        path("", views.employee_login),
        path("home/", views.employee_view),
        path("register/", views.employee_register)
        ]