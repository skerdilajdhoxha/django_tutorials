"""djangotutorials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tutorials.views import home, about, contact, tutorial_list, tutorial_detail, video_detail, category_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^tutorials/$', tutorial_list, name='tutorial'),
    # url(r'^$', tutorial_detail, name='tutorial_detail'),
    url(r'^tutorials/(?P<slug>[\w-]+)/$', tutorial_detail, name='tutorial_detail'),
    url(r'^tutorials/(?P<slug>[\w-]+)/(?P<pk>\d+)/$', video_detail, name='video_detail'),
    #url(r'^categories/$', category, name='category'),
    url(r'^(?P<slug>[\w-]+)/$', category_detail, name='category_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

