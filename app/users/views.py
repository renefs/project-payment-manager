from django.shortcuts import render

# Create your views here.
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from users.forms import ProfileEditForm

def login_user(request):
    username = password = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/profile')
            else:
                return HttpResponseRedirect('/user-not-active')
    return render_to_response('users/login.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def profile_user(request):
    return render(request, 'users/profile.html')

@login_required(login_url='/login/')
def edit_user_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            return HttpResponseRedirect('/profile/')
    else:
        form = ProfileEditForm()
    return render(request, 'users/profile-edit.html', {'form': form})