from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.gallery,name='gallery'),
    path('photo/<photo_id>',views.photo,name='photo'),
    path('search/', views.search_results, name='search_results'),
    path('location/<location_id',views.filter_by_location,name='location')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
