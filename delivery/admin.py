from django.contrib import admin
from .models import Delivery


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone', 'status')
