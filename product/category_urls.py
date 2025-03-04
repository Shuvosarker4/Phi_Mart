from product import views
from django.urls import path

urlpatterns = [
    path('',views.view_category,name='category-list'),
    path('<int:pk>/',views.view_specific_category,name='view-specific-category')
]