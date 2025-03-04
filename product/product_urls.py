from product import views
from django.urls import path

urlpatterns = [
    path('',views.ViewProduct.as_view(),name='products-list'),
    path('<int:pk>/',views.ViewSpecificProduct.as_view(),name='product-list'),
]