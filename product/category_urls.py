from product import views
from django.urls import path

urlpatterns = [
    path('',views.ViewCategory.as_view(),name='category-list'),
    path('<int:pk>/',views.ViewSpecificCategory.as_view(),name='view-specific-category')
]