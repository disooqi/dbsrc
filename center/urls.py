from django.conf.urls import patterns, include, url
from center.views import AboutView
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('center.views',
    url(r'^$', 'index'),
    url(r'^thankyou/$', 'showthankyou'),
    url(r'^contactus/$', 'contact'),    
    url(r'^staff/$', 'showStaff'),
                       
)

urlpatterns += patterns('',
    url(r'^about/$', AboutView.as_view()),  # or
    url(r'^trial/$', TemplateView.as_view(template_name="trial.html")),
    url(r'^bootstrap/$', TemplateView.as_view(template_name="bootstrap_base.html")),
        
)
