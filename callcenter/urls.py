__author__ = 'nick'

from django.conf.urls import url
from callcenter import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.Homepage, name='HomePage'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^editprofile/$', views.editprofile_view, name='editprofile'),  # add redirect to own profile
    ## TODO: check if user is authorized to edit a profile.
    ## TODO: change model etc.for
    ## TODO: automaticaly redirect to needed profile
    url(r'^status/$', views.status_view, name='status'),
    ## TODO: somehow get the ip to check status from
    ## TODO: check tablet status, AND check voiceconference status
    ## TODO: create placeholder interface and link to troubleshoot
    url(r'^vc_create/$', views.create_vc, name='vc_create')
]