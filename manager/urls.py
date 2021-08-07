from django.conf.urls import url

from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [

    path('', views.index, name='index'),
    path('statistic', views.statistic, name='statistic'),
    path('logout', views.logout_view, name='logout'),
    path('setting', views.setting, name='setting'),
    url(r'^login/$', views.user_login, name='login'),
    #path('accounts/', include('django.contrib.auth.urls')),                   # Добавили новый маршрут
    path('reg/', views.registr, name='reg'),                  # Добавили новый маршрут
    path('mail/', views.mail, name='mail'),                  # mail
]