from django.conf.urls import patterns, include, url
from rango import views
<<<<<<< HEAD
=======
from django.conf import settings
>>>>>>> 6baa26752e8d40a0bd67c6fef3874401ffa360a6

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tangorango.views.home', name='home'),
    # url(r'^tangorango/', include('tangorango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', include(admin.site.urls))
)
<<<<<<< HEAD
=======


if settings.DEBUG:
<<<<<<< HEAD
urlpatterns += patterns('django.views.static', (r'media/(?P<path>.*)','serve', {'document_root': settings.MEDIA_ROOT}), )
>>>>>>> 6baa26752e8d40a0bd67c6fef3874401ffa360a6
=======
	urlpatterns += patterns(
		'django.views.static', 
		(r'media/(?P<path>.*)',
		'serve', 
		{'document_root': settings.MEDIA_ROOT}), )
>>>>>>> fce9085fd4847fe600a5c0017812675c2500a1be
