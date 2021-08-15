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
    path('news/', views.news, name='news'),                  # Добавили новый маршрут
    path('group/', views.group, name='group'),                  # Добавили новый маршрут
    path('add_news/', views.add_news, name='add_news'),                  # Добавили новый маршрут
    path('edit_news/<int:id_post>', views.edit_news, name='edit_news'),                  # Добавили новый маршрут
    path('delete_news/<int:id_post>', views.delete_news, name='delete_news'),                  # Добавили новый маршрут
    path('mail/', views.mail, name='mail'),                  # mail


    path('profile/<int:profileid>', views.profile, name='profile'),                  # mail
    path('new/<int:post>', views.new_post, name='new_post'),                  # mail
    path('profile/<name>', views.myprofile, name='myprofile'),                  # mail


    #api
    path('api/login', views.api_login, name='api/login'),


    #Администрирование
    path('admins/user', views.admin_user, name='admins/admins'),
]