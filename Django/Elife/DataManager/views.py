from django.http import HttpResponse
from django.shortcuts import render
from models import Audio,UserAudioBehavior,User
import simplejson,json
import re
# Create your views here.

def object2dict(obj):
        d={}
        d['__class__'] = obj.__class__.__name__
        d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return d


# def getAudio(request):
#     if request.method=='POST':
#         print request.body
#         data=simplejson.loads(request.body)
#         print data
#         # lists=Audio.objects.filter(audioTitle=data['audioTitle'])
#         lists=Audio.objects.filter(id=1)
#         # print lists
#         # print lists.__dict__
#         # return HttpResponse({'error_code':0,'reason':'return successfully','data':lists.__dict__})
#         if lists.count()==0:
#             return HttpResponse(simplejson.dumps(simplejson.dumps({'error_code':1,'reason':'No corresponding data in database','data':[]})))
#         else:
#             return_list=[]
#             for list in lists:
#                 # dict={'audioId':list.audioId,'audioUrl':list.audioUrl,'audioTitle':list.audioTitle,'audioDate':list.audioDate,
#                 #       'audioText':list.audioText,'audioImgUrl':list.audioImageUrl,'audioLrcUrl':list.audioLrcUrl,'audioType':list.audioType,
#                 #       'audioPartEndTime':list.audioPartEndTime,'audioTextBlankIndex':list.audioTextBlankIndex,'avgCorrectRate':list.avgCorrectRate}
#                 # return_list.append(dict)
#
#             #     dict=list.__dict__
#             #     print dict
#             #     for key,d in dict.keys():
#             #         t=d
#             #         dict[key]=str(t)
#             #     print dict
#             #     return_list.append(dict)
#             #
#                 # print list.__dict__
#                 # # print type(list.__dict__)
#                 # json = simplejson.dumps(list.__dict__)
#                 # print json
#                 print list.audioText
#                 list.audioUrl= 'http://192.168.235.33:8000/player'
#                 list.audioPartEndTime= [10000, 20000, 30000]
#                 s = list.__dict__
#                 # print s
#                 return_list.append(s)
#                 print 'finish'
#
#
#
#             # print return_list
#
#             # print return_list
#             dict_str = {'error_code':"0",'reason':'return successfully','data':return_list}
#
#             return_dict=simplejson.dumps(str(dict_str))
#             return HttpResponse(return_dict)
#     else:
#         return HttpResponse(simplejson.dumps({'error_code':1,'reason':'NO POST!','data':[]}))


def player(req,ID):
    audio=Audio.objects.get(audioId=ID)
    audio_data =open(audio.audioUrl, "rb").read()
    return HttpResponse(audio_data, "audio.audioUrl")

def showImg(req,ID):
    img=Audio.objects.get(audioId=ID)
    img_data =open(img.audioImageUrl, "rb").read()
    return HttpResponse(img_data, "img.audioImageUrl")

def showLrc(req,ID):
    lrc=Audio.objects.get(audioId=ID)
    lrc_data =open(lrc.audioLrcUrl, "rb").read()
    return HttpResponse(lrc_data, "audio.audioLrcUrl")

def getAudio(request):
    if request.method=='POST':
        data=simplejson.loads(request.body)
        print data
        try:
            list=Audio.objects.get(audioId=data['audioId'])
            dict=list.__dict__
            # print dict
            del dict['_state']
            dict['audioUrl']='http://192.168.235.33:8000/player/%s/'%list.audioId
            dict['audioImageUrl']='http://192.168.235.33:8000/showImg/%s/'%list.audioId
            dict['audioLrcUrl']='http://192.168.235.33:8000/showLrc/%s/'%list.audioId
            dict['audioText']='a'

            s=dict['audioPartEndTime'].split('##')
            print 1,s
            dict['audioPartEndTime']=s
            print 2,dict['audioPartEndTime']
            s1=changeToList(dict['audioTextBlankIndex'])
            print 3,s1
            dict['audioTextBlankIndex']=s1
            print 4,dict['audioTextBlankIndex']
            s2=changeToList(dict['audioStandardAnswer'])
            print 5,s2
            dict['audioStandardAnswer']=s2
            print 6,dict['audioStandardAnswer']
            # print 8,dict
            # print 9,return_dict
            return_dict={'error_code':'0','reason':'return successfully','data':dict}
            return HttpResponse(simplejson.dumps(return_dict))
        except:
            return_dict={'error_code':'1','reason':'No corresponding data in database','data':[]}
            return HttpResponse(simplejson.dumps(simplejson.dumps(return_dict)))


    else:
        return HttpResponse(simplejson.dumps({'error_code':'1','reason':'NO POST!','data':[]}))


def showLists(request):
    if request.method=='POST':
        print 0,request.body
        data=simplejson.loads(request.body)

        print 1,data
        print 2,type(data)

        print 3,data['userId']
        print 4,type(data['userId'])

        # userId=re.sub("-","",data['userId'])
        # print 5,userId

        user=User.objects.get_or_create(userId=data['userId'],userWrongWords="",userCorrectRate=0)


        audios=Audio.objects.all()[:20]
        audio_list=[]
        for audio in audios:
            dict={'audioId':audio.audioId,'audioTitle':audio.audioTitle,
                  'audioImageUrl':'http://192.168.235.33:8000/showImg/%s/'%audio.audioId,
                  'audioDate':audio.audioDate}
            audio_list.append(dict)
            print 6,'http://192.168.235.33:8000/showImg/%s/'%audio.audioId
        return_dict={'error_code':'0','reason':'return successfully','data':audio_list}
        return HttpResponse(simplejson.dumps(return_dict))
    else:
        return HttpResponse(simplejson.dumps({'error_code':'1','reason':'NO POST!','data':[]}))


def returnStandardAnswer(request):
    if request.method=='POST':
        data=simplejson.loads(request.body)
        audio=Audio.objects.get(audioId=data['audioId'])
        user=User.objects.get(userId=data['userUUID'])
        userAnswer=data['userAnswer']
        rate=audioCorrectRate(userAnswer,audio.audioId)
        behavior=UserAudioBehavior.objects.get_or_create(audioId=audio.audioId,userId=user.userId,
                                                         userAnswer=userAnswer,audioCorrectRate=rate)
        dict={'audioId':audio.audioId,'audioStandardAnswer':audio.audioStandardAnswer}
        return_dict={'error_code':'0','reason':'return successfully','data':dict}
        return HttpResponse(simplejson.dumps(return_dict))
    else:
        return HttpResponse(simplejson.dumps({'error_code':'1','reason':'NO POST!','data':[]}))




def audioCorrectRate(userAnswer,ID):
    audio=Audio.objects.get(audioId=ID)

    standardAnswer=audio.audioStandardAnswer
    s_list=standardAnswer.split('$$')[0:3]
    for i in range(s_list.__len__()):
        s=s_list[i].split('##')
        s1=s[0:s.__len__()-1]
        s_list[i]=s1
    u_list=userAnswer.spilt('##')
    for i in range(s_list[0].__len__()):
        count=0
        if s_list[0][i]==u_list[i]:
            count+=1
    rate=i*1.0/s_list[0].__len__()

    # s_list=standardAnswer.split('##')
    # s_list=s_list[0:s_list.__len__()-1]

    return rate

def changeToList(s):
    s_list=s.split('$$')[0:3]
    for i in range(s_list.__len__()):
        s=s_list[i].split('##')
        s1=s[0:s.__len__()-1]
        s_list[i]=s1
    return s_list


