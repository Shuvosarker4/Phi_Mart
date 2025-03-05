from product import views
from django.urls import path

urlpatterns = [
    path('',views.ProductList.as_view(),name='products-list'),
    path('<int:pk>/',views.ProductDetails.as_view(),name='product-list'),
]