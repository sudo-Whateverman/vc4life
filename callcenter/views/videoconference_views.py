from callcenter.forms import VCallForm
from callcenter.models import Profile
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

__author__ = 'nick'

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
