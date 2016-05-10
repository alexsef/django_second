from django.conf.urls import include, url
from myblog.views import *
# from django.conf.urls.static import static


urlpatterns = [
    url(r'^snapback/', 'myblog.views.snapback', name='snapback'),
    url(r'^shoes/', 'myblog.views.shoes', name='shoes'),
    url(r'^jackets/', 'myblog.views.jackets', name='jackets'),
    url(r'^jackets-woman/', 'myblog.views.jackets_woman', name='jackets_woman'),
    url(r'^skateboards/', 'myblog.views.skateboards', name='skateboards'),
    url(r'^backpacks/', 'myblog.views.backpacks', name='backpacks'),
    url(r'^glasses/', 'myblog.views.glasses', name='glasses'),
    # url(r'^belts/', 'myblog.views.belts', name='belts'),
    url(r'^snowboards/', 'myblog.views.snowboards', name='snowboards'),
    url(r'^accessories/', 'myblog.views.accessories', name='accessories'),

]
