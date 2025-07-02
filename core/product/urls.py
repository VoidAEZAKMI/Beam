from django.urls import path
from core.product.views import products as v

app_name = "product"

urlpatterns = [
    path("",v.ProductListView.as_view(), name="product_index"),
    path("create/", v.ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/",v.ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/",v.ProductDeleteView.as_view(), name="product_delete"),
]
