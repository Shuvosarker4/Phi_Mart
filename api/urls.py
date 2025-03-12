from product import views
from django.urls import path,include
from rest_framework_nested import routers
from product.views import ProductViewSet,CategoryViewSet,ReviewViewSet
from order.views import CartViewSet,CartItemViewSet

router = routers.DefaultRouter()
router.register('products',ProductViewSet,basename='product-list')
router.register('categories',CategoryViewSet,basename='category-list')
router.register('carts', CartViewSet, basename='carts')

product_router = routers.NestedDefaultRouter(router,'products',lookup = 'product')
product_router.register('reviews',ReviewViewSet,basename='product-review')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(product_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]