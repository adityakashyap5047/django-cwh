from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpadte

# admin.site.register(Product)
# admin.site.register(Contact)
admin.site.register((Product, Contact)) # we can also do it like this
admin.site.register(Orders)
admin.site.register(OrderUpadte)