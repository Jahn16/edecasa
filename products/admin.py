from django.contrib import admin
from .models import Product,Variation,Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(Category)
