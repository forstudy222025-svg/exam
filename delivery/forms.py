from django import forms
from .models import Delivery


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['customer_name', 'phone', 'address', 'status']
        labels = {
            'customer_name': 'Customer Name',
            'phone': 'Phone',
            'address': 'Address',
            'status': 'Status',
        }
        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'Enter customer name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter delivery address', 'rows': 3}),
            'status': forms.Select(),
        }
