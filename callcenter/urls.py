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
    ## status ##
    url(r'^status/pending/$', views.simple_list, {'status': 'P'}, name='pending'),
    url(r'^status/approved/$', views.simple_list, {'status': 'A'}, name='approved'),
    url(r'^status/rejected/$', views.simple_list, {'status': 'R'}, name='rejected'),
    url(r'^status/physical/$', views.status_view_physical, name='physical'),
    ## end status ##
    ## TODO: somehow get the ip to check status from
    url(r'^vc_create/$', views.create_vc, name='vc_create'),
    url(r'^problems/$', views.problem_page, name='problem'),
    url(r'^password_reset/$', views.change_password, name='reset'),
    url(r'^kitsync/$', views.editkits_view, name='kitsync'),
    url(r'^api/$', views.apiuse_view, name='apiuse'),
    url(r'^version/$', views.version, name='version'),
    url(r'^rmxrules/$', views.rmxrules, name='rmxrules'),
    url(r'^test/$', views.test, name='test'),
    ## troubleshooting ##
    url(r'^troubleshoot/diagnostics/$', views.troubleshoot, {'problem': 'diagnostics'}, name='diagnostics'),
    url(r'^troubleshoot/soundprob/$', views.troubleshoot, {'problem': 'sound'}, name='sound'),
    url(r'^troubleshoot/networkprob/$', views.troubleshoot, {'problem': 'web'}, name='web'),
    url(r'^troubleshoot/cameraprob/$', views.troubleshoot, {'problem': 'camera'}, name='camera'),
    url(r'^troubleshoot/videoprob/$', views.troubleshoot, {'problem': 'video'}, name='video'),
    url(r'^troubleshoot/setup/$', views.troubleshoot, {'problem': 'setup'}, name='setup'),
    ## end troubleshooting ##
    url(r'^managecalls/$', views.manage_calls, name='manage_calls'),
    url(r'^manage_calls_by_id/(?P<VC_id>\d+)$', views.manage_calls_by_id, name='manage_calls_by_id'),



]
