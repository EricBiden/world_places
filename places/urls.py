from django.urls import path
from .views import place_list, post_detail, post_category

urlpatterns = [
    path('', place_list, name='place-list'),
    path('detail/<int:id>/', post_detail , name='place_detail'),
    path('category/<int:id>/', post_category , name='place_category')
]
