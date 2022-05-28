from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def gallery(request):
    return render(request,'photos/gallery.html')

def photo(request,photo_id):
    return render(request,'photos/photo.html')