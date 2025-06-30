"""
URL configuration for project10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app1.views import view1,view2,view3,view4,view5,view6
urlpatterns = [
    path('dtl1/', view1),
    path('dtl2/', view2),
    path('dtl3/', view3),
    path('dtl4/', view4),
    path('dtl5/', view5),
    path('dtl6/', view6),
]
