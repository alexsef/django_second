from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
# from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response


def shoes(request):
    shoes = Shoes.objects.all().order_by('title')
    material = Materials.objects.all().order_by('material')
    brands = Brands.objects.all().order_by('brand')
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
    jackets = Jacets.objects.all()
    material = Materials.objects.all().order_by('material')
    brands = Brands.objects.all().order_by('brand')
    context = {
        'brands' : brands,
        'material' : material,
        'jackets' : jackets,
    }
    return render_to_response("jackets.html", context)

def skateboards(request):
    skateboards = Skateboards.objects.all()
    context = {
        'skateboards' : skateboards,
    }
    return render_to_response("skateboards.html", context)

def backpacks(request):
    backpacks = Backpacks.objects.all()
    context = {
        'backpacks' : backpacks,
    }
    return render_to_response("backpacks.html", context)

def belts(request):
    belts = Belts.objects.all()
    context = {
        'belts' : belts,
    }
    return render_to_response("belts.html", context)

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


