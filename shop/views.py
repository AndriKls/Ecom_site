from django.shortcuts import render
from .models import Products, Order
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


def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        county = request.POST.get('county', '')
        zipcode = request.POST.get('zipcode', '')
        total = request.POST.get('total', '')

        order = Order(items=items, name=name, email=email, address=address, city=city, county=county, zipcode=zipcode, total=total)
        order.save()
    return render(request, 'shop/checkout.html')