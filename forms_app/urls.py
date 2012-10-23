from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('forms_app.views',
    url(r'^thanks/$', TemplateView.as_view(template_name="forms/thanks.html")),
    url(r'^$', "contact"),
                       
)

