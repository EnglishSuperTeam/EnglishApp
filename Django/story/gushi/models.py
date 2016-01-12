from django.db import models

# coding:utf-8


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class AudioInfo(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    content = models.TextField()
    mp3_path = models.TextField()
    pic_path = models.TextField()


    def __unicode__(self):
        return self.title


class AudioInfo_User(models.Model):
    user = models.ForeignKey(User)
    audioInfo = models.ForeignKey(AudioInfo)
    isGood = models.CharField(max_length=20)
    Question = models.TextField()

    def __unicode__(self):
        audio_user = self.user.name+'_'+self.audioInfo.title
        return audio_user




