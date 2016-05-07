from django.conf.urls import include, url
from django.contrib import admin
# from myblog.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^item/', include('myblog.urls')),
]
