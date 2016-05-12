from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.views.generic import TemplateView
# from django.views.generic import ListView
# from django.views.generic import DetailView
from .models import *
from django.shortcuts import render, render_to_response


def shoes(request):
    shoes = Shoes.objects.order_by('title')
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response("shoes.html", context)


def shoes_price_up(request):
    shoes = Shoes.objects.order_by("price")
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response("shoes.html", context)


def shoes_price_down(request):
    shoes = Shoes.objects.order_by("-price")
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response("shoes.html", context)


def size41(request):
    shoes = Shoes.objects.filter(size_41=True)
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)


def size42(request):
    shoes = Shoes.objects.filter(size_42=True)
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)


def size43(request):
    shoes = Shoes.objects.filter(size_43=True)
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)


def sh_vans(request):
    shoes = Shoes.objects.filter(brand='1')
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)


def sh_dc(request):
    shoes = Shoes.objects.filter(brand='7')
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)


def sh_nike(request):
    shoes = Shoes.objects.filter(brand='8')
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)


def sh_hl(request):
    shoes = Shoes.objects.filter(material='1')
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)


def sh_koj(request):
    shoes = Shoes.objects.filter(material='2')
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)


def sh_zam(request):
    shoes = Shoes.objects.filter(material='3')
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)


def sh_vo(request):
    shoes = Shoes.objects.filter(material='4')
    shoes1 = Shoes.objects.order_by('material')
    shoes2 = Shoes.objects.order_by('brand')
    context = {
        'shoes' : shoes,
        'shoes1' : shoes1,
        'shoes2' : shoes2,
    }
    return render_to_response('shoes.html', context)









def shoes_new(request):
    shoes = Shoes.objects.order_by("created")
    material = Materials.objects.order_by('material')
    brands = Brands.objects.order_by('brand')
    context = {
        'brands' : brands,
        'shoes' : shoes,
        'material' : material,
    }
    return render_to_response("shoes.html", context)


def snapback(request):
    snapback = Goods.objects.all()
    brands = Brands.objects.all().order_by('brand')
    context = {
        'brands' : brands,
        'snapback' : snapback,
    }
    return render_to_response("snapback.html", context)


def jackets(request):
    jackets_man = Jacets.objects.filter(sex='man')
    
    material = Materials.objects.all().order_by('material')
    brands = Brands.objects.all().order_by('brand')
    context = {
        'brands' : brands,
        'material' : material,
        'jackets' : jackets_man,
    }
    return render_to_response("jackets.html", context)


def jackets_woman(request):
    jackets_woman = Jacets.objects.filter(sex='woman')
    material = Materials.objects.all().order_by('material')
    brands = Brands.objects.all().order_by('brand')
    context = {
        'brands' : brands,
        'material' : material,
        'jackets' : jackets_woman,
    }
    return render_to_response("jackets.html", context)


def skateboards(request):
    skateboards = Skateboards.objects.all()
    brands = Brands.objects.all().order_by('brand')
    context = {
        'brands' : brands,
        'skateboards' : skateboards,
    }
    return render_to_response("skateboards.html", context)

def backpacks(request):
    backpacks = Backpacks.objects.all()
    context = {
        'backpacks' : backpacks,
    }
    return render_to_response("backpacks.html", context)


def snowboards(request):
    snowboards = Snowboards.objects.all()
    context = {
        'snowboards' : snowboards,
    }
    return render_to_response("snowboards.html", context)

def glasses(request):
    glasses = Spectacles.objects.all()
    context = {
        'glasses' : glasses,
    }
    return render_to_response("glasses.html", context)

def accessories(request):
    accessories = Accessories.objects.all()
    context = {
        'accessories' : accessories,
    }
    return render_to_response("accessories.html", context)


