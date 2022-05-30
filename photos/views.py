from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Location, Poster,Category, Photo

# Create your views here.
def gallery(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()
    location = request.GET.get('location')
    if location ==None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(location__location=location)
    locations = Location.objects.all()
    context = {'photos':photos, 'categories':categories, 'locations':locations}
    return render(request,'photos/gallery.html', context)

def photo(request,photo_id):
    try:
        photo = Photo.objects.get(id= photo_id)
    except:
        raise Http404()
    return render(request,'photos/photo.html',{'photo':photo})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})