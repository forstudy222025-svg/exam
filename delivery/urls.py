from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeliveryListView.as_view(), name='delivery_list'),
    path('add/', views.DeliveryCreateView.as_view(), name='delivery_add'),
    path('<int:pk>/edit/', views.DeliveryUpdateView.as_view(), name='delivery_edit'),
    path('<int:pk>/delete/', views.DeliveryDeleteView.as_view(), name='delivery_delete'),
    path('api/', views.deliveries_api, name='delivery_api'),
]
