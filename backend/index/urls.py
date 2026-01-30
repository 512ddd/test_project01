from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import (
    IndexView, CustomerViewSet, VendorViewSet, StoreViewSet,
    ProductViewSet, ProductMediaViewSet, OrderViewSet,
    OrderItemViewSet, OrderStatusViewSet, CommentViewSet,
    CartItemViewSet, WishlistItemViewSet, SearchHistoryViewSet
)

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-media', ProductMediaViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'order-status', OrderStatusViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'wishlist-items', WishlistItemViewSet)
router.register(r'search-history', SearchHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]
