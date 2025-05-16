from django.shortcuts import render
from .models import Place

def place_list(request):
    places = Place.objects.all()
    return render(request, 'places/index.html', {'places': places})
