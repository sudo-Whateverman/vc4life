from callcenter.forms import VCallForm
from callcenter.models import Profile, VideoCall, VCkit
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils import timezone

__author__ = 'nick'

@login_required()
def create_vc(request):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    if request.method == "POST":
        form = VCallForm(data=request.POST, pikud_form=obj.pikud, location_form=obj.location)
        if form.is_valid():
            ## TODO : add check that people can be invited.
            vcall = form.save(commit=False)
            vcall.vc_head = obj
            vcall.request_time = timezone.now()
            #vcall.VC_id = str(vcall.VC_id.int)[0:7]
            vcall.save()
            form.save_m2m()
            return redirect('/')
        else:
            return redirect('/problems/')
    else:
        if obj.location is not None:
            form = VCallForm(pikud_form=obj.pikud, location_form=obj.location)
        else:
            return redirect('/problems/')
        ## TODO: show only people the person can actually invite
        ## TODO: add line completion widget to names so typing would be fast
        return render(request, 'vc_create.html', {'form': form})

def manage_calls(request):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    calls = VideoCall.objects.filter(vc_head=obj)
    # form_calls = list()
    # for call in calls:
    #     if call.starting_time > timezone.now() and call.ending_time < timezone.now():
    #         form_calls.append(call)
    return render(request, 'manage.html', {'calls': calls})

def manage_calls_by_id(request, VC_id):
    obj = VideoCall.objects.get(VC_id=VC_id)
    participants = obj.participants.all()
    return render(request, 'managebyid.html', {'obj': obj, 'participants': participants})
