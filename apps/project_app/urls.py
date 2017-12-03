from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.travels),
    url(r'^add$', views.add_plan),
    url(r'^process_travel$', views.process_travel),
    url(r'^destination/(?P<id_>\d+)$', views.destination),
    url(r'^join/(?P<team_id>\d+)$', views.join),
    url(r'^remove/(?P<team_id>\d+)$', views.remove),

  ]
