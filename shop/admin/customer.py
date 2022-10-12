from django.contrib import admin

from shop.models import customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'name',
        'email',
    )
    list_display_links = (
        'id',
        'name',
    )
    fields = (
        'user',
        'name',
        'email',
    )


admin.site.register(customer.Customer, CustomerAdmin)
