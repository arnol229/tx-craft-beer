from django.conf.urls import *
from django.contrib import admin
from views import home, index, brewery, brewpub, bar, beer
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', home),
	#(r'^contact/$', contact),
	#index
	(r'^index/$', index),
	#(r'^search/$', search),
	#specifics
	(r'^brewery/(?P<id>[/d]+)/$', brewery),
	(r'^brewpub/(?P<id>[/d]+)/$', brewpub),
	(r'^bar/(?P<id>[/d]+)/$', bar),
	(r'^beer/(?P<id>[/d]+)/$', beer),
	)
	

urlpatterns += patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root':settings.STATIC_ROOT, "show_indexes":True}),
	)