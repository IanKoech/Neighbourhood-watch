from django.shortcuts import *
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'all-hoody/index.html')

