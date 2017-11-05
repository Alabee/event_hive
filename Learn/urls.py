"""Learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from home import views as home
from django.contrib import admin
from register import views as register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.index),
    url(r'^home/', include('home.urls')),
    url(r'^events/', include('event_details.urls')),
    url(r'^review/', include('review.urls')),
    url(r'^register/', include('register.urls')),
    url(r'^login/', register.login, name ='login'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)