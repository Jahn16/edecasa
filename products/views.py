from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product

class HomeProductListView(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'
    queryset = Product.objects.values('slug', 'name', 'base_price', 'image')[:9]

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_object(self):
        product = super(ProductDetailView, self).get_object()
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        images = [product.image, product.second_image, product.third_image, product.fourth_image]
        context['product_images'] = list(filter(None, images))
        return context
