from django.shortcuts import render
from .models import Place, Category
from django.http import Http404


def place_list(request):
    places = Place.objects.all()
    places = Place.objects.get(id=1)
    places_last = Place.objects.all().order_by('-id')[:4]
    places_pinned = Place.objects.filter(is_pinned=True)[:4]
    places_popullar = Place.objects.filter(popullar=True)[:4]
    beautifull = Place.objects.filter(beautifull=True)[:6]
    return render(request, 'main/index.html', {'places': places, 'places_last': places_last, 'places_pinned': places_pinned, 'places_popullar': places_popullar, 'beautifull': beautifull})


def post_detail(request, id):
    try:
        post = Place.objects.get(id=id)
    except Place.DoesNotExist:
        raise Http404()
    return render(request, 'places/single.html', {'post':post})

def post_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Place.DoesNotExist:
        raise Http404()
    places = Place.objects.filter(category=category)
    return render(request, 'main/home-3.html', {'place_category':category, 'places': places}) 