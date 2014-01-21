from django.shortcuts import render

# Create your views here.
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from projects.models import Proyecto

from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from django.views.generic.detail import DetailView
from django.utils import timezone


class ProyectoDetailView(DetailView):

    model = Proyecto

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context