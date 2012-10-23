from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
    url(r'^current$', 'getCurrentPoll')
)

