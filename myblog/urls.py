from django.conf.urls import include, url
from myblog.views import *


urlpatterns = [
    # url(r'^$', home.as_view(template_name = 'index.html') name="home"),
    url(r'^$', 'myblog.views.home'),
]
