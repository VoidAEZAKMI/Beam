from rest_framework import viewsets

from core.product.models.products import (
    Supplier, Product, Category, Customer, Order, OrderItem
)

from .serializers import (
    SupplierSerializer, ProductSerializer, CategorySerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer
)

class SupplierViewSet(viewsets.ModelViewSet):
    """
    Роут для модели Поставщик
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
