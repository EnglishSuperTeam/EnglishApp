from django.shortcuts import render,render_to_response

from django import forms
from django.http import HttpResponse,StreamingHttpResponse

# Create your views here.

class UserForm(forms.Form):
    username=forms.CharField()
    headImg=forms.FileField()

def register(request):
    if request.method=="POST":
        uf=UserForm(request.POST,request.FILES)
        if uf.is_valid():
            return HttpResponse('upload ok!')
    else:
        uf=UserForm()
    return render_to_response('register.html',{'uf':uf})


def big_file_download(request):
    def file_iterator(file_name,chunk_size=512):
        with open(file_name) as f:
            while True:
                c=f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name='file_name.txt'
    response=StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="test.pdf"'
    return response