from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from PIL import Image
from os.path import join
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    base_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')
    second_image = models.ImageField(upload_to='product_images', blank=True)
    third_image = models.ImageField(upload_to='product_images', blank=True)
    fourth_image = models.ImageField(upload_to='product_images', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        def optimize_image(image):

            image_path = join(settings.MEDIA_ROOT, image.name)
            image_pillow = Image.open(image_path)
            image_pillow.save(image_path, optime=True, quality=85)

        def resize_image(image):

            max_image_width, max_image_height = (640, 640)
            image_path = join(settings.MEDIA_ROOT, image.name)
            image_pillow = Image.open(image_path)
            image_width, image_height = image_pillow.size
            if image_width != max_image_width or image_height != max_image_height:
                resized_image = image_pillow.resize((max_image_width, max_image_height), Image.LANCZOS)
                resized_image.save(image_path)

        def generate_slug():
            slug = slugify(self.name) + str(self.pk)
            return slug

        if not self.slug:
            self.slug = generate_slug()
        super().save(*args, **kwargs)
        for image in [self.image, self.second_image, self.third_image, self.fourth_image]:
            if image:
                optimize_image(image)
                resize_image(image)





class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
