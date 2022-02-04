from cgi import test
from django.urls import path, include
from .views import ProductListView

app_name = "products"

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list')
]
