from django.conf.urls import patterns, include, url

from django.views.static import * 
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Town_Country.views',
	url(r'^$', 'home', name='home'),
	url(r'^about/$', 'about'),
	url(r'^contact/$', 'contact')
	
)

urlpatterns += patterns('',
    # Examples:
     url(r'^properties/', include('properties.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
