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
    #path('accounts/', include('django.contrib.auth.urls')),                   #
    path('reg/', views.registr, name='reg'),                  #
                    # т
    path('group/', views.group, name='group'),                  #
    path('profile_group/<int:id_profile>', views.profile_group, name='profile_group'),                  #
              # Д

    #Course
    path('add_course/', views.add_course, name='add_course'),
    path('edit_course/<int:id>', views.edit_course, name='edit_course'),
    path('delete_course/<int:id_profile>', views.delete_course, name='delete_course'),
    path('course_qvant/', views.course_qvant, name='course_qvant'),
    path('course/', views.course, name='course'),
    path('info_course/<int:id>', views.info_course, name='info_course'),
    path('info_qvant/<slug:name>', views.info_qvant, name='info_qvant'),

    #news
    path('edit_news/<int:id_post>', views.edit_news, name='edit_news'),                  # Д
    path('delete_news/<int:id_post>', views.delete_news, name='delete_news'),                  #
    path('news/', views.news, name='news'),
    path('new/<int:post>', views.new_post, name='new_post'),
    path('add_news/', views.add_news, name='add_news'),


    path('profile/<int:profileid>', views.profile, name='profile'),                  #
    path('profile/<name>', views.myprofile, name='myprofile'),                  #


    path('bid/', views.bid, name='bid'),

    #api
    path('api/login', views.api_login, name='api/login'),
    path('mail/', views.mail, name='mail'),

    #Администрирование
    path('admins/user', views.admin_user, name='admins/admins'),
]