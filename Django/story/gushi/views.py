#coding=utf-8

from django.shortcuts import render,HttpResponse,render_to_response,HttpResponsePermanentRedirect
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from gushi.models import User
# Create your views here.

def play(request):

    return HttpResponse('play.html')

class UserForm(forms.Form):
    name = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',max_length=20)



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


                return render_to_response('successLogin.html',{'name':name})
            except ObjectDoesNotExist:
                return HttpResponsePermanentRedirect('/login/')

    else:
        uf=UserForm()
        return render_to_response('login.html',{'uf':uf})





