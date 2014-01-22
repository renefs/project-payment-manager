from django.shortcuts import render

# Create your views here.
from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from users.forms import ProfileEditForm
from users.models import UserProfile, DatosFacturacion
from django.contrib.auth.models import User


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


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def profile_user(request):

    user = request.user

    return render(request, 'users/profile.html',{'username': user.username})


@login_required
def edit_user_profile(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            #Datos del usuario
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.email = cd['email']

            #Perfil
            try:
                profile = user.get_profile()

                profile.datosFacturacion.first_name=cd['billing_first_name'],
                profile.datosFacturacion.last_name=cd['billing_last_name'],
                profile.datosFacturacion.cif_nif=cd['billing_cif'],
                profile.datosFacturacion.city=cd['billing_city'],
                profile.datosFacturacion.address=cd['billing_address'],
                profile.datosFacturacion.province=cd['billing_province'],
                profile.datosFacturacion.country=cd['billing_country']

            except UserProfile.DoesNotExist:

                datos_facturacion = DatosFacturacion.objects.create(
                    first_name=cd['billing_first_name'],
                    last_name=cd['billing_last_name'],
                    cif_nif=cd['billing_cif'],
                    city=cd['billing_city'],
                    address=cd['billing_address'],
                    province=cd['billing_province'],
                    country=cd['billing_country']
                )

                profile = UserProfile.objects.create(
                    user=user, website=cd['website'], datosFacturacion=datos_facturacion
                )

            user.save()
            profile.save()

            return HttpResponseRedirect('/profile/')
    else:

        try:
            profile = user.get_profile()

            form = ProfileEditForm(initial={
                'first_name': profile.user.first_name,
                'last_name': profile.user.last_name,
                'email': profile.user.email,
                'website': profile.website,
                'billing_first_name': profile.datosFacturacion.first_name,
                'billing_last_name': profile.datosFacturacion.last_name,
                'billing_cif': profile.datosFacturacion.cif_nif,
                'billing_city': profile.datosFacturacion.city,
                'billing_address': profile.datosFacturacion.address,
                'billing_province': profile.datosFacturacion.province,
                'billing_country': profile.datosFacturacion.country
            }
            )

        except UserProfile.DoesNotExist:

            userProfile = None

            form = ProfileEditForm(initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email, })

    return render(request, 'users/profile-edit.html', {'form': form, 'username': user.username})