from django.shortcuts import render
from django.conf import settings



def index(request):

    return render(request,'manager/index.html',{"name":"name","msg":"msg"})


def statistic(request):
    print("kirill")
    return render(request,'manager/statistic.html',{"name":"name","msg":"msg"})


def reg(request):
    print("kirill")
    return render(request,'manager/reg.html',{"name":"name","msg":"msg"})
