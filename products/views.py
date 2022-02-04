import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    template_name = "products/product_list.html"
    queryset = Product.objects.all()
    context_object_name = "products"

class ProductDetailView(generic.DetailView):
    template_name = "products/product_detail.html"
    queryset = Product.objects.all()
    context_object_name = "product"