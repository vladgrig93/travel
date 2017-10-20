from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.index),
    url(r'^newpage$', views.display),#page displayed after logging in or registering, redirected to after logging in or registering
    url(r'^newpage_reg$', views.register),#register processing url
    url(r'^newpage_log$', views.login),#login processing url
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^process$', views.process),
    url(r'^destination/(?P<trip_id>\d+)$', views.goto),
    url(r'^jointripprocess/(?P<trip_id>\d+)$', views.jointripprocess)
    ]