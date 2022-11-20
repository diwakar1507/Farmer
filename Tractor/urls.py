from django.contrib import admin
from django.urls import path
from Tractor import views
urlpatterns = [
    path("", views.home, name='home'),
    path("/", views.home, name='home'),
    path("details", views.details, name='details'),
]
