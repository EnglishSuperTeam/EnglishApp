#coding=utf-8
__author__ = 'root'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Elife.settings')
import django
django.setup()
import urllib2
import simplejson
from DataManager.models import Audio


server_url='http://127.0.0.1:8000/getAudio/'
data={'audioId':'20160122178','userId':1}
data2=simplejson.dumps(data)
request = urllib2.Request(url=server_url,data=data2)

response = urllib2.urlopen(request)
get_response_string = response.read()
d=simplejson.loads(get_response_string)
print d



# audio=Audio.objects.get(audioTitle='听如果能再爱一次cd1-01')
# a=audio.__dict__
# for key in a.keys():
#     print key,a[key]

