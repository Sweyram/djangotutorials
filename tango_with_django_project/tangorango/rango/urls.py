from django.conf.urls import patterns, include, url
from rango import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
<<<<<<< HEAD
<<<<<<< HEAD
	url(r'^about$', views.about, name = 'about'),
=======
	url(r'^/about/', views.about, name = 'about'),
>>>>>>> 6baa26752e8d40a0bd67c6fef3874401ffa360a6
=======
	url(r'^about/', views.about, name = 'about'),
>>>>>>> fce9085fd4847fe600a5c0017812675c2500a1be
)
