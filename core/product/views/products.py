from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from core.product.models.products import Product


class WSNotifyMixin:
    group = "notifications"
    def _ws_send(self, text: str) -> None:
        layer = get_channel_layer()
        async_to_sync(layer.group_send)(self.group, {"type": "send_notification", "message": text})


class JSONMixin(WSNotifyMixin):
    def form_valid(self, form):
        create = self.object is None
        response = super().form_valid(form)   # <-- возвращаем HTML-редирект
        action = "создан" if create else "обновлён"
        self._ws_send(f"Товар «{self.object}» {action}.")
        return response

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        self._ws_send(f"Товар «{obj}» удалён.")
        return super().delete(request, *args, **kwargs)


class ProductListView(ListView):
    model               = Product
    template_name       = "products/index.html"
    context_object_name = "products"


class ProductCreateView(JSONMixin, CreateView):
    model  = Product
    fields = ("name", "price")
    success_url = reverse_lazy("product:product_index")


class ProductUpdateView(JSONMixin, UpdateView):
    model  = Product
    fields = ("name", "price")
    success_url = reverse_lazy("product:product_index")


class ProductDeleteView(JSONMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("product:product_index")