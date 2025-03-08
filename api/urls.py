from product import views
from django.urls import path,include
from rest_framework_nested import routers
from product.views import ProductViewSet,CategoryViewSet,ReviewViewSet

router = routers.DefaultRouter()
router.register('products',ProductViewSet,basename='product-list')
router.register('categories',CategoryViewSet,basename='category-list')

product_router = routers.NestedDefaultRouter(router,'products',lookup = 'product')
product_router.register('reviews',ReviewViewSet,basename='product-review')



urlpatterns = [
    path('',include(router.urls)),
    path('',include(product_router.urls)),
]