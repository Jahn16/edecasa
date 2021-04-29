from django.urls import path
from .views import HomeProductListView,ProductDetailView
app_name = 'products'

urlpatterns = [
    path('', HomeProductListView.as_view(), name='home'),
    path('<slug>', ProductDetailView.as_view(),name='detail'),

]