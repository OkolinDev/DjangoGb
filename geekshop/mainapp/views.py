from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, ProductCategory


def main(request):
    title = 'Главная'

    products = Product.objects.all()

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }

    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    product = get_object_or_404(Product, pk=pk)
    content = {
        'title': title,
        'links_menu': links_menu,
        'product': product,

    }
    return render(request, 'mainapp/product.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')
