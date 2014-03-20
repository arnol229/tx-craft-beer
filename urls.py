from django.conf.urls.defaults import *
from django.contrib import admin
from views import home, index, contact, brewery, brewpub, bar, beer


admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'home', name='home'),
	(r'^view/(?P<subject>[/w]+)/$', 'index', name='index'),
	(r'^contact/$', 'contact', name='contact'),
	(r'^brewery/(?P<id>[/d]+)/$', 'brewery', name='brewery'),
	(r'^brewpub/(?P<id>[/d]+)/$', 'brewpub', name='brewpub'),
	(r'^bar/(?P<id>[/d]+)/$', 'bar', name='bar'),
	(r'^beer/(?P<id>[/d]+)/$', 'beer', name='beer'),
	)