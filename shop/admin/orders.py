from django.contrib import admin

from shop.models import order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'date_ordered',
        'complete',
        'transaction_id',
    )
    list_display_links = (
        'id',
        'transaction_id',
    )
    fields = (
        'customer',
        'complete',
        'transaction_id',
    )
    readonly_fields = (
        'date_ordered',
    )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'order',
        'quantity',
        'date_added',
    )
    list_display_links = ('id',)
    fields = (
        'product',
        'order',
        'quantity',
    )


admin.site.register(order.OrderItem, OrderItemAdmin)
admin.site.register(order.Order, OrderAdmin)
