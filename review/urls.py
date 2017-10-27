from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'review'),
	url(r'^art/', views.art, name = 'art'),
	url(r'^partying/',views.partying, name = 'partying'),
	url(r'^conferences/', views.conferences, name = 'conferences'),
	url(r'^tech/', views.tech, name = 'tech'),

]
