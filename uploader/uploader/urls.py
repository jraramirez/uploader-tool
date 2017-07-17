"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# from . import views
from file_loader import views

urlpatterns = [
    
    # Link to types of uploads
    url(r'^uploader/', include([
        url(r'^$', views.index, name='index'),
        url(r'^shift/', include('shift.urls')),
        url(r'^auto/(?P<uploader_name>[a-z]+)/$', views.auto_upload, name='auto_upload'),
    ])),

    # Manager urls
    url(r'^manager/', include('manager.urls')),
]
