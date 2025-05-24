from django.contrib import admin
from .models import Place, Category, PlaceImage


admin.site.register(Category)
admin.site.register(PlaceImage)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name','image','category', 'latitude','longitude', 'is_pinned', 'popullar', 'beautifull']
