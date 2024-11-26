from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('checkout/', views.checkout, name='checkout' )
]
