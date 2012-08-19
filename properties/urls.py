from django.conf.urls import patterns, include, url

urlpatterns = patterns('properties.views',

     url(r'^$', 'index'),
     #url(r'^properties/(?P<properties_id>\d+)/$', 'properties.views.detail')
)
