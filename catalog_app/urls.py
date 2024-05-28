from .views import product
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('products/', product.product_list, name='product_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)