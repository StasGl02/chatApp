from django.shortcuts import render
from .models import *
import datetime


def home(request):
    try:
        MessageInfo.objects.get(pk=1)
    except MessageInfo.DoesNotExist:
        MessageInfo(id=1, username='', message='').save()
        StatInfo(id=1, count=0).save()
        StatInfo(id=2, count=0).save()
    msinfo = MessageInfo.objects.get(pk=1)
    bro = StatInfo.objects.get(pk=1)
    sis = StatInfo.objects.get(pk=2)
    return render(request, 'chatapp/home.html', {'bro': bro, 'sis': sis, 'msinfo': msinfo})


def login(request):
    bro = StatInfo.objects.get(pk=1)
    sis = StatInfo.objects.get(pk=2)
    return render(request, 'chatapp/home.html', {'bro': bro, 'sis': sis})


def sendinfo(user, mess):
    msinfo = MessageInfo.objects.get(pk=1)
    msinfo.username = '{0} at {1}'.format(user, datetime.datetime.now().strftime('%H:%M'))
    msinfo.message = mess
    msinfo.save()
    return msinfo


def addbro(request):
    bro = StatInfo.objects.get(pk=1)
    sis = StatInfo.objects.get(pk=2)
    bro.count += 1
    bro.save()
    msinfo = sendinfo(request.user.username, 'Bro!')
    return render(request, 'chatapp/home.html', {'bro': bro, 'sis': sis, 'msinfo': msinfo})


def addsis(request):
    bro = StatInfo.objects.get(pk=1)
    sis = StatInfo.objects.get(pk=2)
    sis.count += 1
    sis.save()
    msinfo = sendinfo(request.user.username, 'Sis!')
    return render(request, 'chatapp/home.html', {'bro': bro, 'sis': sis, 'msinfo': msinfo})
