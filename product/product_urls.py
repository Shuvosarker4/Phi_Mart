from product import views
from django.urls import path

urlpatterns = [
    path('',views.view_products,name='products-list'),
    path('<int:pk>/',views.view_specific_product,name='product-list'),
]