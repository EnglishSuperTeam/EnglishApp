from django.db import models

# Create your models here.

class Audio(models.Model):
    audioId=models.CharField(max_length=20,primary_key=True)
    audioTitle=models.CharField(max_length=100)
    audioType=models.CharField(max_length=20)
    audioDate=models.CharField(max_length=20,blank=True)
    audioUrl=models.CharField(max_length=80)
    audioImageUrl=models.CharField(max_length=80)
    audioLrcUrl=models.CharField(max_length=80)
    audioText=models.TextField()
    audioPartEndTime=models.CharField(max_length=50)
    audioTextBlankIndex=models.TextField(blank=True)
    audioStandardAnswer=models.TextField(blank=True)
    avgCorrectRate=models.FloatField(max_length=10,blank=True)

    def __unicode__(self):
        return self.audioId



class User(models.Model):
    userId=models.CharField(max_length=50,primary_key=True)
    userWrongWords=models.TextField(blank=True)
    userCorrectRate=models.FloatField(max_length=8,blank=True)

    def __unicode__(self):
        return self.userId

class UserAudioBehavior(models.Model):
    audioId=models.ForeignKey(Audio)
    userId=models.ForeignKey(User)
    isCollected=models.BooleanField(default=False)
    userAnswer=models.TextField(blank=True)
    audioCorrectRate=models.FloatField(max_length=8,blank=True)

    def __unicode__(self):
        return self.userId+'_'+self.audioId

class Word(models.Model):
    wordId=models.CharField(max_length=20,primary_key=True)
    word=models.CharField(max_length=50)
    audioIdList=models.TextField()

    def __unicode__(self):
        return self.word
