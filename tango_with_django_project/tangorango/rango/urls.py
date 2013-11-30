from django.conf.urls import patterns, include, url
from rango import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
<<<<<<< HEAD
	url(r'^about$', views.about, name = 'about'),
=======
	url(r'^/about/', views.about, name = 'about'),
>>>>>>> 6baa26752e8d40a0bd67c6fef3874401ffa360a6
)
