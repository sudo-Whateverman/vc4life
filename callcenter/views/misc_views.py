from callcenter.check_by_ip_interface import check
from callcenter.forms import ApiUseForm, VersionForm, RmxrulesForms
from callcenter.models import ApiUse, VCversion, Rmxrules
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

__author__ = 'nick'
@login_required()
def homepage(request):
    return render(request, 'index.html')

# Add this view
@login_required()
def about_page(request):
    return render(request, 'about.html')

@login_required()
def problem_page(request):
    return render(request, 'problems.html')

@login_required()
def status_view_physical(request):
    marks = check('127.0.0.1')
    return render(request, 'statusphys.html', {'marks': marks})

@login_required()
def troubleshoot(request):
    return render(request, 'troubleshoot.html')

@login_required()
def test(request):
    return render(request, 'base_david.html')

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

@login_required()
def apiuse_view(request):
    obj = ApiUse.objects.first()
    if request.method == 'POST':
        form = ApiUseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ApiUseForm(instance=obj)
    return render(request, 'apiuse.html', {'form': form})

@login_required()
def version(request):
    obj = VCversion.objects.first()
    if request.method == 'POST':
        form = VersionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VersionForm(instance=obj)
    return render(request, 'apiuse.html', {'form': form})

@login_required()
def rmxrules(request):
    obj = Rmxrules.objects.first()
    if request.method == 'POST':
        form = RmxrulesForms(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RmxrulesForms(instance=obj)
    return render(request, 'apiuse.html', {'form': form})