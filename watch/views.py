from django.shortcuts import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'all-hoody/index.html')

def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm()
        
    return render(request, 'create_profile.html', {'form': form})

