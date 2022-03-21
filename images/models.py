from django.db import models
from django.conf import settings
# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="image_created" ,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to="image/%Y/%m/%d")
    description = models.TextField(blank=True) 
    created = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title