from django.conf.urls import *
from django.contrib import admin
from views import home, index, contentProfile, contentHome,contact
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', home),
	#contact
	(r'^contact/$', contact),
	#index
	(r'^index/$', index),
	#content home views
	(r'^(?P<subject>)/(?P<region>[a-zA-Z]+)/$', contentHome),
	(r'^(?P<subject>)/$', contentHome),
	#specific content views
	(r'^(?P<subject>)/(?P<id>[/d]+)/$', contentProfile),
)

	

urlpatterns += patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root':settings.STATIC_ROOT}),
	)