from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ecommerce_drf.products import views

urlpatterns = [
    path('', views.ProductList.as_view(), name="products")
]
urlpatterns = format_suffix_patterns(urlpatterns)
