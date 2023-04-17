"""project25 URL Configuration

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_accessrecords/',insert_accessrecords,name='insert_accessrecords'),
    path('display_topic/',display_topic,name='display_topic'),
    path('display_webpage/',display_webpage,name='display_webpage'),
    path('single_select_web/',single_select_web,name='single_select_web'),
    path('checkbox_web/',checkbox_web,name='checkbox_web'),
    path('radio_webpage/',radio_webpage,name='radio_webpage'),
    path('display_access/',display_access,name='display_access'),
    path('single_select_access/',single_select_access,name='single_select_access'),
    path('checkbox_access/',checkbox_access,name='checkbox_access'),
    path('radio_access/',radio_access,name='radio_access'),
]
