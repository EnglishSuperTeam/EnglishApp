"""csvt01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index/$','blog.views.index'),
    url(r'^view/$','blog.views.current_url_view'),
    url(r'^display1/$','blog.views.ua_display_good1'),
    url(r'^display2/$','blog.views.ua_display_good2'),
    url(r'^displaymeta','blog.views.display_meta'),
    url(r'^search-form/$','blog.views.search_form'),
    url(r'^register/$','blog.views.register'),
    url(r'^disk/$','disk.views.register'),
    )


