from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:customer_id>/', views.customer_overview, name='customer_overview'),
    path('<int:customer_id>/<int:invoice_id>/', views.customer_invoice_detail, name='customer_invoice_detail'),
    # path('<int:customer_id>/tk<int:token_id>/', views.customer_token_detail, name='customer_token_detail'),
]