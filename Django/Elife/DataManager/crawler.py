#coding=utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Elife.settings")
import django
django.setup()
import re
from urllib import urlopen, urlretrieve
import chardet
import eyed3
from DataManager.models import Audio

class Method():

    # 进行解码和编码方法
    def getCode(self, url):
        text = urlopen(url).read()
        c = chardet.detect(text)
        code = c['encoding']
        text = str(text).decode(code, 'ignore').encode('utf-8').replace('\r\n', '')
        return text

    # 爬取网页链接
    def getPageUrl(self, url):
        text = self.getCode(url)
        #获取包含电影链接的代码段
        pattern_code = re.compile(r'<div class="lmflbot bg">.*?</div>')
        url_code = re.findall(pattern_code, text)
        # print 'url_code:', url_code[0]
        pattern_url = re.compile(r'<a href="(.*?)" Title')
        url_list = re.findall(pattern_url, url_code[0])
        return url_list

    #获取故事链接
    def getMovieUrlAndTitle(self, url):
        text = self.getCode(url)
        #爬取包含链接和标题的代码段
        pattern_code = re.compile(r'<div class="lm2flbot2">.*?</div>')
        url_code = re.findall(pattern_code, text)
        # print 'url_code:', url_code[0]
        #爬取链接
        pattern_url = re.compile(r'<a href="(.*?)" Title')
        url_list = re.findall(pattern_url, url_code[0])
        #爬取标题
        pattern_title = re.compile(r'Title="(.*?)" target')
        title_list = re.findall(pattern_title, url_code[0])
        dict = {'title':title_list, 'url': url_list}
        return dict

    #爬取mp3和lrc的链接
    def getMP3AndLrcUrl(self, url):
        text = self.getCode(url)
        mp3 = re.findall(r"var mp3url = '(.*?)'", text)[0]
        lrc = re.findall(r"var texturl ='(.*?)'", text)[0]
        dict = {'mp3': mp3, 'lrc': lrc}
        return dict

    def getTitle(self, title):
        pattern_1 = u'听电影MP3学英语之'
        pattern_2 = u'附中英双语LRC字幕和文本'
        pattern_3 = u' 中英双语MP3+LRC+文本'
        pattern_4 = u'中英双语MP3+LRC'
        pattern_5 = u' 原版MP3+中英LRC字幕'
        pattern_6 = u'听电影MP3学英语 '
        pattern_7 = u'MP3+中英文LRC字幕'
        pattern_8 = u'BBC迷你剧'
        pattern_9 = u'电影Mp3对白学英语'
        title = title.decode('utf-8')
        title = re.sub(pattern_4,'',title).replace(pattern_5,'').replace(pattern_6,'').replace(pattern_7,'')
        title = re.sub(pattern_1,'',title).replace(pattern_2,'').replace(pattern_3,'').replace(pattern_8,'')
        title = re.sub(pattern_9,'',title)
        title = title.encode('utf-8')
        return title

    def getMP3(self, index, url):
        mp3_path = r'/home/zlx/Elife/mp3/' + str(index) + '.mp3'
        urlretrieve(url, mp3_path)
        audio = eyed3.load(mp3_path)
        time = audio.info.time_secs
        dict = {'path': mp3_path, 'time': time}
        return dict

    def getLrc(self, index, url):
        lrc_path = r'/home/zlx/Elife/lrc/' + str(index) + '.lrc'
        urlretrieve(url, lrc_path)
        return lrc_path

    def getContent(self, lrc_path):
        text = self.getCode(lrc_path)
        # print text
        #删除无用内容
        text = re.sub('\[00:00.00.*?mp3/', '', text)
        text = re.sub('\[00:00.01.*?hand', '', text).replace('◎', '').replace('- ', '')
        # print text
        #将文章按句分开
        content_list = re.split(r'\[.*?\]', text)
        pattern_zg = re.compile(u'[\u4e00-\u9fa5]')
        pattern_en = re.compile(u'(.*?) \(*[a-zA-Z]*"*-*《*“*\d*[\u4e00-\u9fa5]')
        content = ''
        for item in content_list:
            if item != '':
                # print item
                text = item.decode('utf-8')
                if re.findall(pattern_zg, text) != []:
                    en = re.findall(pattern_en, text)[0]
                    zg = text.replace(en, '')
                    content = content + en + '##' + zg + '##'
                else:
                    content = content + item + '####'
        return content.encode('utf-8')


    def getDate(self, url):
        text = self.getCode(url)
        date = re.findall(r'<div id="N_small"><span>.*?</span>', text)[0]
        date = re.sub(r'<div id="N_small">.*?:', '', date)
        date = re.sub(r'</span>', '', date)
        return date


    def getArticle(self,index, num, title, mp3_path, lrc_url, url):
        title = self.getTitle(title)
        print 'title: ', title
        date = self.getDate(url)
        type = 'movie'
        print 'type: ', type
        print 'date: ', date
        print 'mp3_path: ', mp3_path
        lrc_path = self.getLrc(index, lrc_url)
        print 'lrc_path: ', lrc_path
        content = self.getContent(lrc_path)
        audio=Audio(audioTitle=title,audioDate=date,audioType=type,audioUrl=mp3_path,audioLrcUrl=lrc_path,audioText=content,
                    avgCorrectRate=0,audioId='20160121'+str(num).zfill(3),audioImageUrl='none',audioPartEndTime='none',audioTextBlankIndex='none')
        audio.save()

if __name__ == '__main__':
    a = Method()
    url_list = a.getPageUrl('http://www.rrting.net/English/movie_mp3/')
    title_list = []
    movie_list = []
    for index in range(1, 10):
        url = 'http://www.rrting.net' + url_list[index]
        dict = a.getMovieUrlAndTitle(url)
        title_list = title_list + dict['title']
        movie_list = movie_list + dict['url']
        # print dict['title'][0]
    num = 0
    for index in range(11, 100):
        url = 'http://www.rrting.net' + movie_list[index] + 'mp3para.js'
        movie_url = 'http://www.rrting.net' + movie_list[index]
        dict_url = a.getMP3AndLrcUrl(url)
        mp3_url = dict_url['mp3']
        # print mp3_url
        mp3_info = a.getMP3(index, mp3_url)
        time = mp3_info['time']
        if time <= 300:
            print time
            a.getArticle(index, num, title_list[index], mp3_info['path'], dict_url['lrc'], movie_url)
            num = num + 1
    print num



