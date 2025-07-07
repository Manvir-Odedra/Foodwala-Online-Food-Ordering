from django.contrib import admin
from home.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(CartItem)

admin.site.register(OrderItem)