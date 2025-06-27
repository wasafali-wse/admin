from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('customer00<int:customer_id>/', views.customer_overview, name='customer_overview'),
    path('customer00<int:customer_id>/invoice00<int:invoice_id>/', views.customer_invoice_detail, name='customer_invoice_detail'),
    # path('<int:customer_id>/tk<int:token_id>/', views.customer_token_detail, name='customer_token_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)