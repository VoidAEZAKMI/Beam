from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from core.product.models.products import (
    Supplier, Category, Product,
    Customer, Order, OrderItem
)


class WSNotifyMixin:
    """Отправка текстовых уведомлений всем в группу «notifications»."""
    group = "notifications"

    def _ws_send(self, text: str) -> None:
        layer = get_channel_layer()
        async_to_sync(layer.group_send)(
            self.group,
            {"type": "send_notification", "message": text},
        )


class JSONNotifyMixin(WSNotifyMixin):
    """
    Заменяет redirect на JSON-ответ (для AJAX) + шлёт WebSocket-уведомление.
    Для DeleteView WebSocket идёт до фактического удаления.
    """
    entity: str | None = None       


    def form_valid(self, form):
        create = self.object is None
        response = super().form_valid(form)          
        action = "создан" if create else "обновлён"
        self._ws_send(f"{self.entity} «{self.object}» {action}.")
        return response


    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        self._ws_send(f"{self.entity} «{obj}» удалён.")
        return super().delete(request, *args, **kwargs)


class SupplierListView(ListView):
    model               = Supplier
    template_name       = "product/supplier_list.html"
    context_object_name = "suppliers"


class SupplierCreateView(JSONNotifyMixin, CreateView):
    model       = Supplier
    fields      = ("name",)
    entity      = "Поставщик"
    success_url = reverse_lazy("product:supplier_index")


class SupplierUpdateView(JSONNotifyMixin, UpdateView):
    model       = Supplier
    fields      = ("name",)
    entity      = "Поставщик"
    success_url = reverse_lazy("product:supplier_index")


class SupplierDeleteView(JSONNotifyMixin, DeleteView):
    model       = Supplier
    entity      = "Поставщик"
    success_url = reverse_lazy("product:supplier_index")


class CategoryListView(ListView):
    model               = Category
    template_name       = "product/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(JSONNotifyMixin, CreateView):
    model       = Category
    fields      = ("name",)
    entity      = "Категория"
    success_url = reverse_lazy("product:category_index")


class CategoryUpdateView(JSONNotifyMixin, UpdateView):
    model       = Category
    fields      = ("name",)
    entity      = "Категория"
    success_url = reverse_lazy("product:category_index")


class CategoryDeleteView(JSONNotifyMixin, DeleteView):
    model       = Category
    entity      = "Категория"
    success_url = reverse_lazy("product:category_index")


class ProductListView(ListView):
    model               = Product
    template_name       = "product/product_list.html"
    context_object_name = "products"


class ProductCreateView(JSONNotifyMixin, CreateView):
    model       = Product
    fields      = ("name", "price", "supplier", "categories")
    entity      = "Товар"
    success_url = reverse_lazy("product:product_index")


class ProductUpdateView(JSONNotifyMixin, UpdateView):
    model       = Product
    fields      = ("name", "price", "supplier", "categories")
    entity      = "Товар"
    success_url = reverse_lazy("product:product_index")


class ProductDeleteView(JSONNotifyMixin, DeleteView):
    model       = Product
    entity      = "Товар"
    success_url = reverse_lazy("product:product_index")



class CustomerListView(ListView):
    model               = Customer
    template_name       = "product/customer_list.html"
    context_object_name = "customers"


class CustomerCreateView(JSONNotifyMixin, CreateView):
    model       = Customer
    fields      = ("name",)
    entity      = "Клиент"
    success_url = reverse_lazy("product:customer_index")


class CustomerUpdateView(JSONNotifyMixin, UpdateView):
    model       = Customer
    fields      = ("name",)
    entity      = "Клиент"
    success_url = reverse_lazy("product:customer_index")


class CustomerDeleteView(JSONNotifyMixin, DeleteView):
    model       = Customer
    entity      = "Клиент"
    success_url = reverse_lazy("product:customer_index")


class OrderListView(ListView):
    model               = Order
    template_name       = "product/order_list.html"
    context_object_name = "orders"


class OrderCreateView(JSONNotifyMixin, CreateView):
    model       = Order
    fields      = ("customer",)
    entity      = "Заказ"
    success_url = reverse_lazy("product:order_index")


class OrderUpdateView(JSONNotifyMixin, UpdateView):
    model       = Order
    fields      = ("customer",)
    entity      = "Заказ"
    success_url = reverse_lazy("product:order_index")


class OrderDeleteView(JSONNotifyMixin, DeleteView):
    model       = Order
    entity      = "Заказ"
    success_url = reverse_lazy("product:order_index")


class OrderItemListView(ListView):
    model               = OrderItem
    template_name       = "product/orderitem_list.html"
    context_object_name = "items"


class OrderItemCreateView(JSONNotifyMixin, CreateView):
    model       = OrderItem
    fields      = ("order", "product", "quantity")
    entity      = "Позиция заказа"
    success_url = reverse_lazy("product:orderitem_index")


class OrderItemUpdateView(JSONNotifyMixin, UpdateView):
    model       = OrderItem
    fields      = ("order", "product", "quantity")
    entity      = "Позиция заказа"
    success_url = reverse_lazy("product:orderitem_index")


class OrderItemDeleteView(JSONNotifyMixin, DeleteView):
    model       = OrderItem
    entity      = "Позиция заказа"
    success_url = reverse_lazy("product:orderitem_index")
