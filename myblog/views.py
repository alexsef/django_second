# from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.views.generic import TemplateView
from django.shortcuts import render


# class home(TemplateView):
    # pass

def home(request):
    template_name = "index.html"
    return render(request, template_name)
