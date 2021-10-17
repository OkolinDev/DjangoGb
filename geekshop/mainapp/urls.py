from django.urls import path

import mainapp.views
from mainapp.views import products, contact, product

urlpatterns = [
    path('category/<int:pk>/', products, name='category'),
    path('', products, name='index'),
    path('product/<int:pk>/', product, name='products'),

    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
]


