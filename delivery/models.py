from django.db import models


class Delivery(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('in_progress', 'قيد التوصيل'),
        ('delivered', 'تم التوصيل'),
        ('cancelled', 'ملغى'),
    ]

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.customer_name

    class Meta:
        permissions = [
            ('can_manage_delivery', 'Can manage delivery'),
        ]
