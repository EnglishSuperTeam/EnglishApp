#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import User,Book,Users
from django import forms
# Create your views here.

#users=User.objects.get(name="")
# def index(request):
#     # return render_to_response('index.html',{'users':users.n})
#     return render_to_response('')

users=User.objects.all()


def index(request):
    return render_to_response('index.html',{"users":users})

def current_url_view(request):
    return HttpResponse("Welcome to page at %s"%request.path)

def ua_display_good1(request):
    try:
        ua=request.META['HTTP_USER_AGENT']
    except KeyError:
        ua='unknown'
    return HttpResponse('Your browser is at %s'%ua)

def ua_display_good2(request):
    ua=request.META.get('HTTP_USER_AGENT','unknown')
    return HttpResponse('Your browser is at %s'%ua)

def display_meta(request):
    values=request.META.items()
    values.sort()
    html=[]
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

class UserForm(forms.Form):
    username=forms.CharField(label='用户名：',max_length=100)
    password=forms.CharField(label='密码：',widget=forms.PasswordInput())
    email=forms.EmailField(label='电子邮件：')


def register(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            email=uf.cleaned_data['email']
            user=Users()
            user.username=username
            user.password=password
            user.email=email
            user.save()

            return render_to_response('success.html',{'username':username})
    else:
        uf=UserForm()
        return render_to_response('register.html',{'uf':uf})