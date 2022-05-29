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
    except:
        raise Http404()
    return render(request,'photos/photo.html',{'photo':photo})

def filter_by_location(request,location_id):
    
    #filters by location
    photos = Photo.filter_by_location(id=location_id)
    return render(request,'location.html',{'photos':photo})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})