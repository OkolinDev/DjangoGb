from django.urls import path

import mainapp.views as mainapp
app_name = 'mainapp'

urlpatterns = [
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('', mainapp.products, name='index'),
    path('product/<int:pk>/', mainapp.product, name='product'),

    # path('products/', mainapp.products, name='products'),
    # path('contact/', mainapp.contact, name='contact'),
]


