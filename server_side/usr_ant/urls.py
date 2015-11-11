from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.peerlist, name='peerlist'),
    url(r'^peerlist/$', views.peerlist),
    url(r'^peerlogin/$', views.peerlogin),
    url(r'^groupmanager/$', views.groupmanager),
]
