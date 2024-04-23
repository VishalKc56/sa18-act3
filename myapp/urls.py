from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_index, name='product_index'),
    path('products/<int:id>/', views.product_show, name='product_show'),
]