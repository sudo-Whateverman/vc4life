from django.contrib.auth.views import password_reset

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
    url(r'^status/pending/$', views.status_view, name='pending'),
    url(r'^status/approved/$', views.status_view_approved, name='approved'),
    url(r'^status/rejected/$', views.status_view_rejected, name='rejected'),
    url(r'^status/physical/$', views.status_view_physical, name='physical'),
    ## TODO: somehow get the ip to check status from
    url(r'^vc_create/$', views.create_vc, name='vc_create'),
    url(r'^problems/$', views.problem_page, name='problem'),
    url(r'^troubleshoot/$', views.troubleshoot, name='troubleshoot'),
    url(r'^password_reset/$', views.change_password, name='reset'),
    url(r'^kitsync/$', views.editkits_view, name='kitsync'),
    url(r'^api/$', views.apiuse_view, name='apiuse'),
    url(r'^version/$', views.version, name='version'),
    url(r'^rmxrules/$', views.rmxrules, name='rmxrules'),
    url(r'^test/(?P<status>\w+)$', views.simple_list, name='test'),
]
