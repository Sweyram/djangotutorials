from django.conf.urls import patterns, include, url
from django.contrib import admin
import contacts.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^addressbook/', include('addressbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', contacts.views.ListContactView.as_view(), name = 'contacts-list',),
)
