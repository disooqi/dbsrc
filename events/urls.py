from django.conf.urls import patterns, include, url
from events.models import Article
from django.views.generic import DetailView, ListView

urlpatterns = patterns('events.views',
    url(r'^$', 'news_listing'),
    url(r'^article/(?P<article_id>\d+)/$', 'showArticle'),
)

