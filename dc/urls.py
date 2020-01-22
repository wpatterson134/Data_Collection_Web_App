from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    #/dc/
    re_path(r'^$', views.index, name='index'),

    re_path(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    # re_path((r'dc\\/(?P<media_id>[0-9]+)\\/$'), views.detail, name='detail'),
    re_path(r'^media/add/$', views.MediaCreate.as_view(), name ='mediaCreate'),
    re_path(r'^media/(?P<pk>[0-9]+)/$', views.MediaUpdate.as_view(), name ='updateCreate'),
    re_path(r'^logout_user/$', views.logout_user, name='logout_user'),
    re_path(r'^login_user/$', views.login_user, name='login_user'),
    re_path(r'^register/$', views.register, name='register'),
]
