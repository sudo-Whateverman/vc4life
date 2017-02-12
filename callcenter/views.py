from .models import Profile
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, VCallForm


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
    obj = get_object_or_404(Profile, profile=request.user)
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
    return render(request, 'status.html')

@login_required()
def create_vc(request):
    obj = Profile.objects.get(profile=request.user)
    if obj is None:
        return redirect('/problems/')
    if request.method == "POST":
        form = VCallForm(data=request.POST)
        if form.is_valid():
            vcall = form.save(commit=False)
            vcall.vc_head = obj
            vcall.save()
            return redirect('/')
    else:
        form = VCallForm()
        return render(request, 'vc_create.html', {'form': form})