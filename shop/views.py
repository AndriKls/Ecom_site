from django.shortcuts import render
from .models import Products
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.


class Index(ListView):
    model = Products
    template_name = 'shop/index.html'
    context_object_name = 'products'
    paginate_by = 4


    def get_queryset(self):
        products = super().get_queryset()
        item_name  = self.request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            products = products.filter(title__icontains=item_name)
        return products


class ProductDetail(DetailView):
    model = Products
    template_name ='shop/product_detail.html'
    context_object_name = 'product'

