#coding=utf-8

from django.shortcuts import render,HttpResponse,render_to_response,HttpResponsePermanentRedirect
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from gushi.models import User,AudioInfo
# Create your views here.

def play(request):
    list=AudioInfo.objects.filter(id=1)

    return render_to_response('play.html',{'list':list})

class UserForm(forms.Form):
    name = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',max_length=20)
#
# class AudioInfoForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     date = forms.CharField(max_length=100)
#     content = forms.TextField()
#     mp3_path = forms.TextField()
#     pic_path = forms.TextField()

def register(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            name=uf.cleaned_data['name']
            password=uf.cleaned_data['password']
            user=User()
            user.name=name
            user.password=password
            user.save()

            return render_to_response('successRegister.html',{'name':name})

    else:
        uf=UserForm()
        return render_to_response('register.html',{'uf':uf})

def login(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            name=uf.cleaned_data['name']
            password=uf.cleaned_data['password']
            try:
                user=User.objects.filter(name=name,password=password)
                # if user.exists():

                lists=AudioInfo.objects.all()
                return render_to_response('show.html',{'lists':lists})
            except ObjectDoesNotExist:
                return HttpResponsePermanentRedirect('/login/')

    else:
        uf=UserForm()
        return render_to_response('login.html',{'uf':uf})

def show(request):
    if request.method=='POST':
        check_box=request.POST.getlist('check_box')
        print len(check_box)
        audio=AudioInfo.objects.get(id=check_box[0])
        audio_data=open(audio.mp3_path,'rb').read()
        return HttpResponse(audio_data,'audio.mp3_path')

    else:
        lists=AudioInfo.objects.all()
        return render_to_response('show.html',{'lists':lists})

def test(request):
    return render_to_response('test.html')

def play1(request):
    list=AudioInfo.objects.filter(id=0)
    audio_data=open(list.mp3_path,'rb').read()
    return HttpResponse(audio_data,content_type='0.mp3')