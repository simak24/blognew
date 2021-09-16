from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect



def index(request):
    # return HttpResponse("<h1>Hello DIA People</h1>")
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))
