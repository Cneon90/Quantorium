from django.conf.urls import url

from . import views
from django.urls import path


urlpatterns = [

    path('', views.index, name='index'),
    path('statistic', views.statistic, name='statistic'),
    path('reg', views.reg, name='registration'),
]