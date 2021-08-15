from django.conf import settings
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import * #RegistrForm, LoginForm, settingg
from django.core.mail import send_mail
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from .models import *
from .functional import *
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime as DT
from django.contrib.auth.models import Permission,User
from django.contrib.contenttypes.models import ContentType
from datetime import date, datetime

def init_news(request):
    datas={}
    datas['new'] = novelty.objects.all().order_by('-data').order_by('-time')[:settings.NEWS_COLUMN]
    datas['admins'] = request.user.has_perm('manager.can_admins')
    datas['exit'] = request.user.is_authenticated
    return datas


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))