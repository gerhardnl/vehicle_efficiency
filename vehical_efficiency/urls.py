"""vehical_efficiency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from first.views import home, add_vehicle, update_vehicle, delete_vehicle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('add_vehicle/', add_vehicle, name="add"),
    path('up_vehicle/<str:pk>/', update_vehicle, name="up"),
    path('delete_vehicle/<str:pk>/', delete_vehicle, name="del"),

]
