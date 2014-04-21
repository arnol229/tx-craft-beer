from django.conf.urls import *
from django.contrib import admin
from views import home, index, contentProfile, contentHome,contact,landing
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', landing),
	(r'^home/$', home),
	(r'^admin/', include(admin.site.urls)),
	#contact
	(r'^contact/$', contact),
	#index
	(r'^index/$', index),
	#content home views
	(r'^content/(?P<subject>\w+)/(?P<region>[A-Za-z]+)/$', contentHome),
	(r'^content/(?P<subject>\w+)/$', contentHome),
	#specific content views
	(r'^content/(?P<subject>\w+)/(?P<id>[0-9]+)/$', contentProfile),
)

	
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root':settings.STATIC_ROOT}),
		)