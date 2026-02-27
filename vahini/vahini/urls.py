from django.contrib import admin
from django.urls import path
from vapp import views
urlpatterns = [
    path('', views.calculate_total, name='calculate_total'),
    ]
