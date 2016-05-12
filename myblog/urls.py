from django.conf.urls import url
from myblog.views import *
# from django.conf.urls.static import static


urlpatterns = [
    url(r'^snapback/$', 'myblog.views.snapback', name='snapback'),


    url(r'^shoes/or-price-up/$', 'myblog.views.shoes_price_up', name='shoes_price'),
    url(r'^shoes/or-price-down/$', 'myblog.views.shoes_price_down', name='shoes_price_down'),
    url(r'^shoes/or-new/$', 'myblog.views.shoes_new', name='shoes_new'),
    url(r'^shoes/$', 'myblog.views.shoes', name='shoes'),
    url(r'^shoes/size41$', 'myblog.views.size41', name='size41'),
    url(r'^shoes/size42$', 'myblog.views.size42', name='size42'),
    url(r'^shoes/size43$', 'myblog.views.size43', name='size43'),
    url(r'^shoes/vans$', 'myblog.views.sh_vans', name='sh_vans'),
    url(r'^shoes/dc$', 'myblog.views.sh_dc', name='sh_dc'),
    url(r'^shoes/nike$', 'myblog.views.sh_nike', name='sh_nike'),
    url(r'^shoes/hlopok$', 'myblog.views.sh_hl', name='sh_hl'),
    url(r'^shoes/koja$', 'myblog.views.sh_koj', name='sh_koj'),
    url(r'^shoes/zamsha$', 'myblog.views.sh_zam', name='sh_zam'),
    url(r'^shoes/voilok$', 'myblog.views.sh_vo', name='sh_vo'),


    url(r'^jackets/$', 'myblog.views.jackets', name='jackets'),
    url(r'^jackets-woman/$', 'myblog.views.jackets_woman', name='jackets_woman'),
    url(r'^skateboards/$', 'myblog.views.skateboards', name='skateboards'),
    url(r'^backpacks/$', 'myblog.views.backpacks', name='backpacks'),
    url(r'^glasses/$', 'myblog.views.glasses', name='glasses'),
    url(r'^snowboards/$', 'myblog.views.snowboards', name='snowboards'),
    url(r'^accessories/$', 'myblog.views.accessories', name='accessories'),

]



