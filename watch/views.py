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
        
    return render(request, 'all-hoody/create_profile.html', {'form': form})

def profile(request, username):
    return render(request, 'all-hoody/profile.html')

def create_post(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'all-hoody/post.html', {'form': form})


def neighbourhoods(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'all-hoody/neighbourhoods.html', params)

def create_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'all-hoody/newhood.html', {'form': form})

def join_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')

def leave_neighbourhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')


