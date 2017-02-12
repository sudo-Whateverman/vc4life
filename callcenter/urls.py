__author__ = 'nick'

from django.conf.urls import url
from callcenter import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.homepage, name='HomePage'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^about/$', views.about_page, name='about'),
    url(r'^editprofile/$', views.editprofile_view, name='editprofile'),  # add redirect to own profile
    url(r'^status/$', views.status_view, name='status'),
    url(r'^status/approved/$', views.status_view_approved, name='status'),
    url(r'^status/rejected/$', views.status_view_rejected, name='status'),

    ## TODO: somehow get the ip to check status from
    ## TODO: check tablet status, AND check voiceconference status
    ## TODO: create placeholder interface and link to troubleshoot
    url(r'^vc_create/$', views.create_vc, name='vc_create'),
    url(r'^problems/$', views.problem_page, name='problem')
]