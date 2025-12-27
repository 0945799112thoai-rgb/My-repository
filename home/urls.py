from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.trangchu),
    path('child1/', views.child1)
]
