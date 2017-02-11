__author__ = 'nick'

from django.conf.urls import url
from callcenter import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.Homepage, name='HomePage'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]