from django.urls import path
from . import views

# all paths here will have a 'store/' prefix added by ecommerce/urls.py
urlpatterns = [
    path('category/<str:slug>', views.category),
    path('product/<str:slug>', views.product),
    path('register', views.register),
    path('cart', views.cart),
    path('add_to_cart/<int:product_id>', views.add_to_cart),
    path('delete_from_cart/<int:product_id>', views.delete_from_cart),
    path('checkout', views.checkout),
]