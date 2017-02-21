#coding=utf-8
__author__ = 'root'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","csvt01.settings")
import re
import chardet
import django
django.setup()
from urllib import urlopen
from article.models import Article, Source, ArticleUrl, Tag


# '''
# Django 版本大于等于1.7的时候，需要加上下面两句
# import django
# django.setup()
# 否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
# '''

# import django
# if django.VERSION >= (1, 7):  # 自动判断版本
#     django.setup()


# 爬取海词英语网奇闻轶事1-46页的http，网页源代码以及每一页的url
class PatAnecdoteUrl:

    # 获取海词英语网奇闻轶事1-46页的http
    def getHttp(self):
        Http = []
        for i in range(1, 47):
            http = 'http://en.dict.cn/news/topic/strange/pn%s' % i
            # print http
            Http.append(http)
        return Http

    # 获取海词英语网奇闻轶事1-46页的网址所对应的源代码
    def getText(self):
        total_urls = self.getHttp()
        Text = []
        for total_url in total_urls:
            # print total_url
            text = urlopen(total_url).read()
            c = chardet.detect(text)
            code = c['encoding']
            # print code   # 查询网页的编码方式，code 为utf-8
            text = str(text).decode(code, 'ignore').encode('utf-8')
            # print text
            Text.append(text)
        return Text

    # 获取1-46页每篇奇闻轶事的网址
    def getTotalUrl(self):
        texts = self.getText()
        Url = []
        for text in texts:
            pattern1_url = re.compile('<h2.*?class="ainfo">')
            url_list = re.findall(pattern1_url, text)
            pattern2_url = re.compile('/news/view/\d*')
            url_list = str(url_list)
            url_lists = re.findall(pattern2_url, url_list)
            for url_list in url_lists:
                url_list = 'http://en.dict.cn'+url_list
                # print url_list
                Url.append(url_list)
        # print Url
        return Url

# 获取每篇奇闻轶事的url，title，tag，writer，source，content以及category
class PatAnecdote():

    # 获取每篇奇闻轶事的url和网页源代码
    def getUrl(self, url):
        page = urlopen(url).read()
        charset = chardet.detect(page)
        cod = charset['encoding']
        # print(cod)
        page = str(page).decode(cod, 'ignore').encode("utf-8")
        page = page.replace('&amp;', '&').replace('&gt;', '').replace('&lt;', '')
        return page

    # 获取每篇奇闻轶事的标题
    def getTitle(self, page):
        # page = self.getUrl()
        try:
            pattern_title = re.compile('<title>.*?</title>')
            titles = re.findall(pattern_title, page)
            for title in titles:
                pattern_unuse = re.compile('<.*?>')
                title = re.sub(pattern_unuse, '', str(title))
                title = title.replace('_海词英语', '')
                # print title
                return title
        except IndexError:
            return ''

    # 获取每篇奇闻轶事的时间
    def getTime(self, page):
        # page = self.getUrl()
        try:
            pattern_time = re.compile('<div class="info-date">.*?编辑', re.S)
            times = re.findall(pattern_time, page)
            for time in times:
                pattern_unuse = re.compile('<.*?>')
                time = re.sub(pattern_unuse, '', time).replace('编辑', '').strip()
                # print time
                return time
        except IndexError:
            return ''

    # 获取每篇奇闻轶事的标签
    def getTag(self, page):
        # page = self.getUrl()
        try:
            pattern1_tag = re.compile('<a.*?tag.*?</a>')
            tags = re.findall(pattern1_tag, page)
            for tag in tags:
                pattern_unuse = re.compile('<.*?>')
                tag = re.sub(pattern_unuse, '', tag).strip()
                # Tag.append(tags)
                return tag
        except IndexError:
            return ''

    # 获取每篇奇闻轶事的作者
    def getWriter(self):
        writer = '作者：佚名'
        # print writer
        return writer

    # 获取每篇奇闻轶事的来源
    def getSource(self):
        source = '来源：海词英语-奇闻趣事'
        # print source
        return source

    # 获取每篇奇闻轶事的类别一
    def getCategoryOne(self):
        category_one = 'Fun'
        # print category_one
        return category_one

    # 获取每篇奇闻轶事的类别二
    def getCategoryTwo(self):
        category_two = 'Anecdotes'
        # print category_two
        return category_two

    # 获取每篇奇闻轶事的正文
    def getContent(self, page):
        # page = self.getUrl()
        try:
            pattern_content = re.compile('<div class="info-body">.*?<div class="info-tag">', re.S)
            contents = re.findall(pattern_content, page)
            if not contents:
                return ''
            else:
                for content in contents:
                    content = content.replace('</div>', '\n')
                    content = content.replace('<br>', '\n')
                    pattern_unuse1 = re.compile(r'<div class="pager">.*?<div class="info-tag">', re.S)  # 去掉1,2,3，上一页，下一页这些
                    pattern_unuse2 = re.compile('<.*?>')
                    # pattern_unuse3 = re.compile('英中对照.*?只看中文', re.S)
                    content = re.sub(pattern_unuse1, '', content)
                    content = re.sub(pattern_unuse2, '', content)
                    # content = re.sub(pattern_unuse3, '', content)
                    content = content.strip()
                    # print content
                    return content
        except IndexError:
            return ''

    # 获取每篇奇闻轶事的图片
    def getPicture(self, page):
        # page = self.getUrl()
        try:
            pattern1_picture = re.compile(r'<div class="info-body">.*?<div class="info-tag">', re.S)
            picture = re.findall(pattern1_picture, page)
            pattern2_picture = re.compile(r'\"/attach.*?\"')
            picture = str(picture)
            pictures = re.findall(pattern2_picture, picture)
            if not pictures:
                return ''
            else:
                for picture in pictures:
                    picture = picture.replace('\"', '')
                    picture = 'http://en.dict.cn'+picture
                    # print picture
                    return picture
        except IndexError:
            return ''

    # 输出所有函数
    def getAnecdote(self):
        for url in b.getTotalUrl():
            page = self.getUrl(url)
            title = self.getTitle(page)
            if title == '':
                continue
            time = self.getTime(page)
            tag = self.getTag(page)
            writer = self.getWriter()
            source = self.getSource()
            category_one = self.getCategoryOne()
            category_two = self.getCategoryTwo()
            content = self.getContent(page)
            if content == '':
                continue
            picture = self.getPicture(page)
            print 'url', url
            print 'title', title
            print 'time', time
            print 'tag', tag
            print 'writer', writer
            print 'source', source
            print 'category_one', category_one
            print 'category_two', category_two
            print 'content', content
            print 'picture', picture
        #     anecdote = (url, title, time, tag, writer, source, category_one, category_two, content, picture)
        # return anecdote
            a = Article.objects.get_or_create(title=title, date=time, content=content, image=picture, classification=category_one, type=category_two)
            # article = "".join(a.title)

            a.save()
            article = a.title
            au = ArticleUrl.objects.get_or_create(url=url, is_crawled="yes")
            au.save()
            articleurl = au.url
            # s=Source()
            # s.save()
            # s.name= Article.objects.all()[0:3]
            # s.save()
            # source_articleurl = "".join(tuple(au[0]))
            Source.objects.get_or_create(source_url="http://en.dict.cn/news/topic/strange/", name=source,  crawled_date='2015-08-13', source_article=article, source_articleurl=articleurl)
            Tag.objects.get_or_create(name=tag, tag_article=article)

if __name__ == '__main__':
    b = PatAnecdoteUrl()
    b.getHttp()
    b.getText()
    b.getTotalUrl()
    g = PatAnecdote()
    g.getAnecdote()