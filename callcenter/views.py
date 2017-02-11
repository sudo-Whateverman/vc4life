from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

@login_required()
def Homepage(request):
    return render(request, 'index.html')

# Add this view
@login_required()
def about_page(request):
    return render(request, 'about.html')

@login_required()
def editprofile_view(request):
    return render(request, 'editprofile.html')

@login_required()
def status_view(request):
    return render(request, 'status.html')

@login_required()
def create_vc(request):
    return render(request, 'vc_create.html')
