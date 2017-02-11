from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def login_page(request):
    if request.POST:
        user_name = request.POST['username']
        pass_word = request.POST['password']
        user = authenticate(username=user_name,password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required()
def Homepage(request):
    return render(request, 'index.html')
# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

