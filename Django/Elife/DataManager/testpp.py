__author__ = 'root'
lists=Audio.objects.filter(audioTitle=data['audioTitle'])
dict=list.__dict__
print dict
for key,d in dict.keys():
    t=d
    dict[key]=str(t)
print dict
return_list.append(dict)
