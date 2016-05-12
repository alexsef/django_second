from django.conf.urls import url
from myblog.views import *
# from django.conf.urls.static import static


urlpatterns = [
    url(r'^snapback/$', 'myblog.views.snapback', name='snapback'),

    url(r'^shoes/or-price-up/$', 'myblog.views.shoes_price_up', name='shoes_price'),
    url(r'^shoes/or-price-down/$', 'myblog.views.shoes_price_down', name='shoes_price_down'),
    url(r'^shoes/or-new/$', 'myblog.views.shoes_new', name='shoes_new'),
    url(r'^shoes/$', 'myblog.views.shoes', name='shoes'),

    url(r'^jackets/$', 'myblog.views.jackets', name='jackets'),
    url(r'^jackets-woman/$', 'myblog.views.jackets_woman', name='jackets_woman'),
    url(r'^skateboards/$', 'myblog.views.skateboards', name='skateboards'),
    url(r'^backpacks/$', 'myblog.views.backpacks', name='backpacks'),
    url(r'^glasses/$', 'myblog.views.glasses', name='glasses'),
    url(r'^snowboards/$', 'myblog.views.snowboards', name='snowboards'),
    url(r'^accessories/$', 'myblog.views.accessories', name='accessories'),

]



