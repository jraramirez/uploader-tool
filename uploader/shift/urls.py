from django.conf.urls import url

from . import views

app_name = 'shift'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auto/', views.auto_upload, name='auto_upload'),
    url(r'^upload/', views.upload, name='upload'),
    # url(r'^metadata-change/', views.metadata_change, name='metadata_change'),
]