"""jenismenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import index
from .views import halamanutama
from .views import halamanmenu
from .views import halamanpeta
from .views import halamandetail
from .views import createMenu 
from .views import signup
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", index),
    path("halamanutama/", halamanutama),
    path("halamanmenu/", halamanmenu),
    path("halamanpeta/", halamanpeta),
    path("halamanmenu/<int:id>", halamandetail),
    path("createMenu/",createMenu),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page='login'), name='logout'),
    path("signup/", signup, name='signup'),
]