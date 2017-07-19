from django.conf.urls import url

from . import views

app_name = 'file_loader'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'auto/^(?P<uploader_name>[a-z]+)$', views.auto_upload, name='auto_upload'),
    # url(r'^upload/', views.upload, name='upload'),

]