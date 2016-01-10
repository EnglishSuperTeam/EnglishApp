from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=100)
    date=models.CharField(max_length=30)
    content=models.TextField()
    image=models.TextField()
    classification=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    article_source=models.ManyToManyField('Source')
    article_tag=models.ManyToManyField('Tag')

    def __unicode__(self):
        return self.title

class ArticleUrl(models.Model):
    url=models.URLField()
    is_crawled=models.CharField(max_length=100)
    articleUrl_source=models.OneToOneField('Source')

    def __unicode__(self):
        return self.url

class Source(models.Model):
    source_url=models.URLField()
    name=models.CharField(max_length=300)
    crawled_date=models.CharField(max_length=30)
    source_article=models.ManyToManyField(Article)
    source_articleurl=models.ManyToManyField(ArticleUrl)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=300)
    tag_article=models.ManyToManyField(Article)

    def __unicode__(self):
        return self.name

class User_Tag(models.Model):
    user=models.ForeignKey(User)
    article=models.ForeignKey(Article)
    tag_weight=models.FloatField(max_length=20)

    def __unicode__(self):
        user_tag=self.user.name+'_'+self.article.title
        return user_tag

class User_Article(models.Model):
    user=models.ForeignKey(User)
    article=models.ForeignKey(Article)
    is_good=models.CharField(max_length=20)
    is_bad=models.CharField(max_length=20)
    is_skipped=models.CharField(max_length=20)
    read_date=models.DateField(auto_now_add=True)

    def __unicode__(self):
        user_article=self.user.name+'_'+self.article.title
        return user_article





