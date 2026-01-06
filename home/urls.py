from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login', views.logout_view, name='login'),

    path('trangchu/', views.trangchu),
    path('gioithieu/', views.gioithieu),
    path('lienhe/', views.lienhe),

    path('ping/', views.ping),

    path('minigames/', views.minigames),
    path('monhoc/', views.monhoc),
        path('sinhhoc/', views.sinhhoc),
        path('lichsu/', views.lichsu),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
