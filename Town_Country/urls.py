from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Town_Country.views.home', name='home'),
    # url(r'^Town_Country/', include('Town_Country.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
     
     url(r'^properties/$', 'properties.views.index'),
     #url(r'^properties/(?P<properties_id>\d+)/$', 'properties.views.detail')
)
