from django.db import models

# Create your models here.
from django.db import models
from uuid import uuid4
from PIL import Image
from os.path import join
from django.conf import settings

class Product(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False,unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    base_price = models.FloatField()
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.image:
            max_image_width,max_image_height = (800,800)
            image_path = join(settings.MEDIA_ROOT, self.image.name)
            image_pillow = Image.open(image_path)
            image_width,image_height = image_pillow.size
            new_image_width, new_image_height = image_pillow.size

            if image_width > max_image_width:
                new_image_height = (max_image_width * image_height) / image_width
                new_image_width = max_image_width
            if new_image_height > max_image_height:
                new_image_width = (max_image_height * new_image_width) / new_image_height
                new_image_height = max_image_height
            resized_image = image_pillow.resize((round(new_image_width),round(new_image_height)),Image.LANCZOS)
            resized_image.save(image_path,optimize=True,quality=50)







