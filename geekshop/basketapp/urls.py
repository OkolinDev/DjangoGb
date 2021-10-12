from django.urls import path
import basketapp.views as basketapp
# from .views import basket, basket_add, basket_remove

app_name = 'basketapp'
urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>/', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit'),

]
