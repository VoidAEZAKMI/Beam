from django.urls import path
from core.product.views import products as v

app_name = "product"

urlpatterns = [
    
    path("suppliers/", v.SupplierListView.as_view(),   name="supplier_index"),
    path("suppliers/create/", v.SupplierCreateView.as_view(), name="supplier_create"),
    path("suppliers/<int:pk>/update/", v.SupplierUpdateView.as_view(), name="supplier_update"),
    path("suppliers/<int:pk>/delete/", v.SupplierDeleteView.as_view(), name="supplier_delete"),

    path("categories/", v.CategoryListView.as_view(),   name="category_index"),
    path("categories/create/", v.CategoryCreateView.as_view(), name="category_create"),
    path("categories/<int:pk>/update/", v.CategoryUpdateView.as_view(), name="category_update"),
    path("categories/<int:pk>/delete/", v.CategoryDeleteView.as_view(), name="category_delete"),

    path("", v.ProductListView.as_view(),   name="product_index"),
    path("products/create/", v.ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/update/", v.ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", v.ProductDeleteView.as_view(), name="product_delete"),

    path("customers/", v.CustomerListView.as_view(),   name="customer_index"),
    path("customers/create/", v.CustomerCreateView.as_view(), name="customer_create"),
    path("customers/<int:pk>/update/", v.CustomerUpdateView.as_view(), name="customer_update"),
    path("customers/<int:pk>/delete/", v.CustomerDeleteView.as_view(), name="customer_delete"),

    path("orders/", v.OrderListView.as_view(),   name="order_index"),
    path("orders/create/", v.OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/update/", v.OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete/", v.OrderDeleteView.as_view(), name="order_delete"),

    path("order-items/", v.OrderItemListView.as_view(),   name="orderitem_index"),
    path("order-items/create/", v.OrderItemCreateView.as_view(), name="orderitem_create"),
    path("order-items/<int:pk>/update/", v.OrderItemUpdateView.as_view(), name="orderitem_update"),
    path("order-items/<int:pk>/delete/", v.OrderItemDeleteView.as_view(), name="orderitem_delete"),
]
