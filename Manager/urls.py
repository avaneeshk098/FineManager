from Manager import views
from django.urls import path
from django.conf.urls import url
urlpatterns = [
    path("", views.user_login),
    path("register/", views.register),
    path("home/", views.add_fine),
    path("view_fine/", views.view_fine),
    path("delete_fine/", views.delete_fine),
    path("view_employee/", views.manager_employee_view),
    url('logout/', views.logout)
]

