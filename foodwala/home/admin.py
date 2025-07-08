from django.contrib import admin
from home.models import *

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'subject', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')  # Optional: prevent editing

    # Optional: show fields in detail view
    fields = ('name', 'email', 'number', 'subject', 'message', 'created_at', 'updated_at')
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(CartItem)

admin.site.register(OrderItem)