from django.conf.urls import patterns, include, url

urlpatterns = patterns('properties.views',

     url(r'^$', 'index'),
     url(r'^(?P<property_id>\d+)/$', 'detail')
)
