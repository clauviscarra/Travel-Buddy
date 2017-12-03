from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^log-in$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^register_process$', views.register_process),
    url(r'^logout$', views.logout)
  ]
