from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)
    is_active = models.BooleanField(default=True)
    is_index = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name='childs', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='places/')
    category = models.ForeignKey(Category,
                             related_name='products',
                             on_delete=models.CASCADE)
    latitude= models.FloatField()
    longitude= models.FloatField()
    is_pinned = models.BooleanField(default=False)
    popullar = models.BooleanField(default=False)
    beautifull = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class PlaceImage(models.Model):
    place = models.ForeignKey(Place,
                             related_name='images',
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/')