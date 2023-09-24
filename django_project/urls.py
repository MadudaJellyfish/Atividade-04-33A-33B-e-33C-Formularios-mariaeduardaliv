"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appdobahamut import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('jogos', views.create_jogo),
    path('update_game/<str:pk>/', views.update_jogo, name = "update_game"),
    path('mecânicas', views.create_mecanica),
    path('update_mecanica/<str:pk>/', views.update_mecanica, name = "update_mecanica"),
    path('delete_jogo/<str:pk>/', views.delete_jogo, name = "delete_jogo"),
    path('delete_mecanica/<str:pk>/', views.delete_mecanica, name = "delete_mecanica"),
    path('admin/', admin.site.urls),
]
