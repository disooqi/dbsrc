from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbsrc.views.home', name='home'),
    # url(r'^dbsrc/', include('dbsrc.foo.urls')),
    
    #url(, 'dbsrc.views.addinstructor')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls')),
    url(r'^', include('center.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^forms/', include('forms_app.urls')),
    url(r'^googlee9f47ae9e844275c.html', TemplateView.as_view(template_name="googlee9f47ae9e844275c.html")),
)
