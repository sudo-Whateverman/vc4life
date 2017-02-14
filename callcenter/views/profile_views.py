from callcenter.forms import ProfileForm, ProfileKitForm
from callcenter.models import Profile
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils import timezone

__author__ = 'nick'


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
def editkits_view(request):
    try:
        obj = Profile.objects.get(profile=request.user)
    except ObjectDoesNotExist:
        return redirect('/problems/')
    if request.method == "POST":
        form = ProfileKitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProfileKitForm(pikud_form=obj.pikud)
        return render(request, 'editkits.html', {'form': form})
