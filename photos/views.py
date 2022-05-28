from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Location, Poster,Category

# Create your views here.
def gallery(request):
    return render(request,'photos/gallery.html')

def photo(request,photo_id):
    try:
        photo = Photo.objects.get(id= photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'photos/photo.html',{'photo':photo})

def filter_by_location(request,location_id):
    
    #filters by location
    photos = Photo.filter_by_location(id=location_id)
    return render(request,'location.html',{'photos':photo})