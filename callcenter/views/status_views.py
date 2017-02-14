from callcenter.forms import SimpleTableVideo
from callcenter.models import Profile, VideoCall
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, render_to_response
from django.template import RequestContext

__author__ = 'nick'
@login_required()
def status_view(request):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    calls = VideoCall.objects.filter(status='P', vc_head=obj)
    return render(request, 'status.html', {'calls': calls})

@login_required()
def status_view_pending(request):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    calls = VideoCall.objects.filter(status='P', vc_head=obj)
    return render(request, 'status.html', {'calls': calls})

@login_required()
def status_view_rejected(request):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    calls = VideoCall.objects.filter(status='R', vc_head=obj)
    return render(request, 'status.html', {'calls': calls})

@login_required()
def status_view_approved(request):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    calls = VideoCall.objects.filter(status='A', vc_head=obj)
    return render(request, 'status.html', {'calls': calls})

@login_required()
def simple_list(request, status):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    queryset = VideoCall.objects.filter(status=status, vc_head=obj)
    table = SimpleTableVideo(queryset)
    return render(request, 'simple_list.html', {'table': table})

