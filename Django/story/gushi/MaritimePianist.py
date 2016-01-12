#coding=utf-8
__author__ = 'root'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "story.settings")
import django
django.setup()
from Start import GetUrlMethod, PatStoryMethod
from gushi.models import AudioInfo




class PatMaritimePianist():

     # 爬取网页链接
    def getPageUrl(self):
        startUrl = 'http://www.kekenet.com/video/movie/piano/'
        method = GetUrlMethod()
        page_list = method.getPageUrl(0, startUrl)
        # print 1, page_list
        return page_list

    def getStoryAndMp3Url(self):
        page_list = self.getPageUrl()
        method = GetUrlMethod()
        dict = method.getStoryAndMP3Url(page_list, 'video')
        # story_list = dict['story']
        # mp3_list = dict['mp3']
        # print 3, len(story_list), story_list
        # print 3, len(mp3_list), mp3_list
        return dict

    def getArticle(self):
        dict = self.getStoryAndMp3Url()
        story_list = dict['story']
        mp3_list = dict['mp3']
        for index in range(0, len(story_list)):
            url = story_list[index]
            patstory = PatStoryMethod()
            sc = patstory.getStorySC(url)
            content = patstory.getContent(sc)
            if content != '':
                title = 'MaritimePianist'
                print 1, title
                date = patstory.getDate(sc)
                print 2, date
                mp3_path = patstory.getMP3(mp3_list[index], index, 'MaritimePianist')
                print 3, mp3_path
                pic = "http://pic.kekenet.com/2012/0223/20120223034042496.jpg"
                pic_path = patstory.getPicture(sc, index, 'MaritimePianist', pic)
                print 4, pic_path
                print 5, content

                AudioInfo.objects.get_or_create(title=title, date=date, content=content, mp3_path=mp3_path, pic_path=pic_path)
                # audio.save()






if __name__ == '__main__':
    a = PatMaritimePianist()
    a.getArticle()
