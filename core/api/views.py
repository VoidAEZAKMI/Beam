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

class ProductViewSet(viewsets.ModelViewSet):
    """
    Роут для модели Продукт
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Роут для модели Категории
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    Роут для модели Клиент
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    Роут для модели Заказ
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    Роут для модели Позиция в заказе
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
