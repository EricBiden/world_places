from django.contrib import admin
from .models import Place, Category, PlaceImage

admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PlaceImage)