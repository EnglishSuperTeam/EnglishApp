from django.contrib import admin

# Register your models here.
from article.models import User,Article,User_Article,User_Tag,Tag,Source,ArticleUrl

class User_Admin(admin.ModelAdmin):
    list_display = ('name','id')
admin.site.register(User,User_Admin)

class Article_Admin(admin.ModelAdmin):
    list_display = ('title','id','classification','type')
admin.site.register(Article,Article_Admin)

class Source_Admin(admin.ModelAdmin):
    list_display = ('name','id','crawled_date')
admin.site.register(Source,Source_Admin)

class ArticleUrl_Admin(admin.ModelAdmin):
    list_display = ('url','id')
admin.site.register(ArticleUrl,ArticleUrl_Admin)

class Tag_Admin(admin.ModelAdmin):
    list_display = ('name','id')
admin.site.register(Tag,Tag_Admin)

class User_Article_Admin(admin.ModelAdmin):
    list_display = ('user','article','id')
admin.site.register(User_Article,User_Article_Admin)

class User_Tag_Admin(admin.ModelAdmin):
    list_display = ('user','article','id')
admin.site.register(User_Tag,User_Tag_Admin)