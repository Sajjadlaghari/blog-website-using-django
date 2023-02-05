from django.contrib import admin
from django.urls import path, include
from admin import views

urlpatterns = [
    path('/home', views.adminHome, name="admin-home"),
    path('/form', views.adminForm, name="form"),
    path('/table', views.adminTable, name="table"),
]