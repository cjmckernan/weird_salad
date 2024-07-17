from django.urls import path

from sales.views import SaleCreateView, SaleProcessView, SaleProcessedView

urlpatterns = [
    path('sale_create', SaleCreateView.as_view(), name='sale_create'),
    path('sale_process', SaleProcessView.as_view(), name='sale_process'),
    path('sale_processed', SaleProcessedView.as_view(), name='sale_processed'),
]
