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
from .forms import RegistrForm, LoginForm


def index(request):

    return render(request,'manager/index.html',{"name":"name","msg":"msg"})


def statistic(request):
    print("kirill")
    return render(request,'manager/statistic.html',{"name":"name","msg":"msg"})

def reg(request):
    return render(request, 'manager/reg.html', {"name": "name", "msg": "msg"})


def user_login(request):
    data = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data['res'] = 'Authenticated successfully'
                else:
                    data['res'] = 'Disabled account'
            else:
                data['res'] = 'Invalid login'
    else:
        form = LoginForm()
    return render(request, 'manager/login.html', {'form': form,"data":data})

# Функция регистрации
def registr(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = RegistrForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'manager/reg.html', data)
        else:
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё плохо"
            # Рендаринг страницы
            return render(request, 'manager/reg.html', data)

    else: # Иначе
        # Создаём форму
        form = RegistrForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'manager/reg.html', data)


#Выход из системы
def logout_view(request):
    data = {}
    print("norm")
    data['res'] = "Вышли"
    logout(request)
    return render(request, 'manager/index.html', data)