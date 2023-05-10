from django.contrib import admin
from store.models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order)