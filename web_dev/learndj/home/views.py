from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(request, *args, **kwargs):
    # return HttpResponse()
    return render(request, "home.html")

def scifibooks_view(request,*args, **kwargs):
    my_context = {
        "string_key" : "Hello There",
        "int_key" : "69420"
    }
    return render(request, "scifibooks.html")

def bookpage_view(request, *args, **kwargs):
    # return HttpResponse()
    return render(request, "harrypotter.html")

def authorpage_view(request, *args, **kwargs):
    # return HttpResponse()
    return render(request, "author.html")
    # return HttpResponse("<h1>This is the Contact Page!</h1>")
# Create your views here.
