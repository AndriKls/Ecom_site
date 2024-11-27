from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.header = "KellaPood.ee"
admin.site.site_title = "KellaPood.ee Admin Paneel"
admin.site.index_title = "Tere tulemast KellaPood.ee Admin Paneeli"

class ProductsAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category='Default')

    list_display = ('title', 'price', 'discount_price','category')
    search_fields = ('title',)
    actions = ['change_category_to_default']
    change_category_to_default.short_description = "Default category"
    list_editable = ('price',)

    
admin.site.register(Products, ProductsAdmin)
admin.site.register(Order)