import uuid
from callcenter.check_by_ip_interface import check
from .models import Profile, VideoCall
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, VCallForm
from django.core.exceptions import ObjectDoesNotExist


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

@login_required()
def homepage(request):
    return render(request, 'index.html')

# Add this view
@login_required()
def about_page(request):
    return render(request, 'about.html')

@login_required()
def editprofile_view(request):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=obj)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.profile = request.user
            profile.created_date = timezone.now()
            profile.save()
            return redirect('/')
    else:
        form = ProfileForm(instance=obj)
        return render(request, 'editprofile.html', {'form': form})

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
def create_vc(request):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    if request.method == "POST":
        form = VCallForm(data=request.POST)
        if form.is_valid():
            ## TODO : add check that people can be invited.
            vcall = form.save(commit=False)
            vcall.vc_head = obj
            vcall.save()
            form.save_m2m()
            return redirect('/')
        else:
            return redirect('/problems/')
    else:
        form = VCallForm()
        ## TODO: show only people the person can actually invite
        ## TODO: add line completion widget to names so typing would be fast
        return render(request, 'vc_create.html', {'form': form})

def problem_page(request):
    return render(request, 'problems.html')

def status_view_physical(request):
    marks = check('127.0.0.1')
    return render(request, 'statusphys.html', {'marks': marks})

def troubleshoot(request):
    return render(request, 'troubleshoot.html')