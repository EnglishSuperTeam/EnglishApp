__author__ = 'carrie'
#coding=utf-8
import re
from urllib import urlopen,urlretrieve


class GetUrlMethod():

    # 爬取页面链接
    def getPageUrl(self, num, startUrl):
        page_list = []
        for i in range(1, num):
            http = startUrl +'List_' + str(i) + '.shtml'
            page_list.append(http)
        page_list.append(startUrl)
        # print 1, page_list
        return page_list

    # 获取每个故事的链接
    def getStoryAndMP3Url(self,page_list,type):
        story_list = []
        mp3_list = []
        for page in page_list:
            text = urlopen(page).read()
            text = str(text).replace('\r\n','')
            # 获取故事链接
            matchstr = 'http://www.kekenet.com/' + type + '/2.*?shtml'
            # print matchstr
            b = re.compile(matchstr)
            list = re.findall(b, text)
            # print 2, list
            for story in list:
                # 获取MP3下载地址链接,查看MP3是否存在,若不存在,则该是链接不存储
                mp3_url = story.replace(type, 'mp3')
                text = urlopen(mp3_url).read()
                a = re.search(r'http://xia.*?mp3', text)
                if a != None:
                    story_list.append(story)
                    mp3_list.append(a.group())
        dict = {'story':story_list,'mp3':mp3_list}
        # print 3, story_list
        # print 3, mp3_list
        return dict


class PatStoryMethod():

    # 爬取故事的源代码
    def getStorySC(self,url):
        text = urlopen(url).read()
        sc = str(text)
        sc = re.sub(r'\n', '', sc)
        # print 4, sc
        return sc

     # 爬取每个故事的内容
    def getContent(self,sc):
        a = re.compile('<div class="qh_.*?</div>')
        article = re.findall(a, sc)
        content = ''
        if article != []:
            for item in article:
                item = re.sub(r'<.*?>', '', item).replace('&#39;', "'").replace('&quot;', '"')
                content = content + item + '\r\n'
        else:
            content = ''
        # print 5, content
        return content

    def getTitle(self,content):
        title = re.split('\r\n', content)
        title = title[0]
        # print 6, title
        return title

    # 爬取每个故事的音频
    def getMP3(self, mp3, index, storeAdd):
        mp3_path = r'/home/zlx/Download/story/mp3/' + str(index) + r'.mp3'
        urlretrieve(mp3, mp3_path)
        return mp3_path

    # 爬取每个故事的图片
    def getPicture(self, sc, index, storeAdd,pic):
        pic_url = re.search(r'http://pic.kekenet.*?jpg', sc)
        if pic_url != None:
            pic_url = pic_url.group()
            if len(pic_url) > 100:
                a = re.findall(r'http://pic.kekenet.*?jpeg', pic_url)
                if a == []:
                    b = re.findall(r'http://pic.kekenet.*?JPG', pic_url)
                    if b == []:
                        pic_url =re.findall(r'http://pic.kekenet.*?png', pic_url)[0]
                    else:
                        pic_url = b[0]
                else:
                    pic_url = a[0]
        else:
            pic_url = pic

        if re.findall('png', pic_url) == []:
            pic_path = r'/home/zlx/Download/story/pictures/' + str(index) + r'.jpg'
            urlretrieve(pic_url, pic_path)
        else:
            pic_path = r'/home/zlx/Download/story/pictures/' + str(index) + r'.png'
            urlretrieve(pic_url, pic_path)
        return pic_path

    # 爬取音频上传时间
    def getDate(self, sc):
        date = re.findall(r'<time.*?time>',sc)
        date = re.findall(r':(.*?)</time',date[0])
        date = date[0]
        # print date
        return date