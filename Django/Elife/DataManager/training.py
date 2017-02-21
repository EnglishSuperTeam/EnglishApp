#coding=utf-8
__author__ = 'root'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Elife.settings')
import django
django.setup()
import urllib2
import simplejson
from DataManager.models import Audio
import re

# server_url='http://127.0.0.1:8000/getAudio/'
# data={'audioId':'20160122178','userId':1}
# data2=simplejson.dumps(data)
# request = urllib2.Request(url=server_url,data=data2)
#
# response = urllib2.urlopen(request)
# get_response_string = response.read()
# d=simplejson.loads(get_response_string)
# print d



# audio=Audio.objects.get(audioTitle='听如果能再爱一次cd1-01')
# a=audio.__dict__
# for key in a.keys():
#     print key,a[key]

# s="on##position##it##eternally##grateful##buzz##squeeze##you##in##mission##approach##like##$$messing##that##gather##knew##operation##long##like##there##can##it##what##keep##accessories##times##batteries##transition##over##come##knew##yeah##through##war's##moving##first##$$good##fine##should##i##still##way##even##through##every##you##there's##track##thank##old##decorations##may##kids##own##we'll##parts##and##go##note##leave##time##on##to##$$"
# def changeToStringList(s):
#     s_list=s.split('$$')[0:3]
#     for i in range(s_list.__len__()):
#         s=s_list[i].split('##')
#         s1=s[0:s.__len__()-1]
#         for j in range(len(s1)):
#             s1[j]=int(s1[j])
#         s_list[i]=s1
#     return s_list
# s1=changeToStringList(s)
# print s1

lists=Audio.objects.filter(audioType='speech')
for list in lists:
    s=list.audioImageUrl
    s1=re.sub("_","-",s)
    list.audioImageUrl=s1
    list.save()
    print 'ok'