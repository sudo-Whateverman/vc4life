from callcenter.check_by_ip_interface import check
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

__author__ = 'nick'
@login_required()
def homepage(request):
    return render(request, 'index.html')

# Add this view
@login_required()
def about_page(request):
    return render(request, 'about.html')


def problem_page(request):
    return render(request, 'problems.html')

@login_required()
def status_view_physical(request):
    marks = check('127.0.0.1')
    return render(request, 'statusphys.html', {'marks': marks})

def troubleshoot(request):
    return render(request, 'troubleshoot.html')

def test(request):
    return render(request, 'base_david.html')

def password_reset(request):
    return render(request, 'passwordreset.html')
