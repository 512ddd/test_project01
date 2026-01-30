from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import JsonResponse
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Customer, Vendor, Store, Product, ProductMedia,
    Order, OrderItem, OrderStatus, Comment,
    CartItem, WishlistItem, SearchHistory
)
from .serializers import (
    CustomerSerializer, VendorSerializer, StoreSerializer,
    ProductSerializer, ProductMediaSerializer, OrderSerializer,
    OrderItemSerializer, OrderStatusSerializer, CommentSerializer,
    CartItemSerializer, WishlistItemSerializer, SearchHistorySerializer
)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'code': 200, 'info': 'Hello, World!'})

# DRF ViewSets

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    @action(detail=False, methods=["get"])
    def get_info(self, request):
        customer_id = request.query_params.get("customer_id")
        try:
            customer = Customer.objects.get(id=customer_id)
            serializer = CustomerInfoSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({"error": "用户不存在"}, status=404)
        
        
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['store', 'category', 'brand', 'availability']
    search_fields = ['productName', 'description']
    ordering_fields = ['id', 'price', 'createdDate']

class ProductMediaViewSet(viewsets.ModelViewSet):
    queryset = ProductMedia.objects.all()
    serializer_class = ProductMediaSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ['customer']

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class WishlistItemViewSet(viewsets.ModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class SearchHistoryViewSet(viewsets.ModelViewSet):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer
