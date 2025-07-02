from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SupplierViewSet, ProductViewSet, CategoryViewSet, CustomerViewSet, OrderItemViewSet, OrderViewSet
)


router = DefaultRouter()
router.register(r'supplier', SupplierViewSet)
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderitem', OrderItemViewSet)




urlpatterns = [
    path('', include(router.urls)),
]