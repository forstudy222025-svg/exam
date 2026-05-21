from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from .models import Delivery
from .forms import DeliveryForm


class DeliveryListView(LoginRequiredMixin, ListView):
    model = Delivery
    template_name = 'delivery/delivery_list.html'
    context_object_name = 'deliveries'


class DeliveryCreateView(LoginRequiredMixin, CreateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'delivery/delivery_form.html'
    success_url = reverse_lazy('delivery:delivery_list')


class DeliveryUpdateView(LoginRequiredMixin, UpdateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'delivery/delivery_form.html'
    success_url = reverse_lazy('delivery:delivery_list')


class DeliveryDeleteView(LoginRequiredMixin, DeleteView):
    model = Delivery
    template_name = 'delivery/delivery_confirm_delete.html'
    success_url = reverse_lazy('delivery:delivery_list')


def deliveries_api(request):
    """Return all deliveries as JSON list of objects.

    Accessible at /delivery/api/ and returns fields: customer_name, phone, address, status.
    """
    qs = Delivery.objects.all().values('id', 'customer_name', 'phone', 'address', 'status')
    data = list(qs)
    return JsonResponse(data, safe=False)
