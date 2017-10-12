from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^event_details/', views.event_details, name = 'event_details_form'),
]
