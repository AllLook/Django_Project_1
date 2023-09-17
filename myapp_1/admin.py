from django.contrib import admin

from .models import Order


#
# @admin.action(description='Сброс до 0')
# def reset_quantity(modeladmin, request, queryset):
#     queryset.update(quantity=0)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'orders', 'order_price']
    ordering = ['customer']
    list_filter = ['date_added_order', 'order_price']
    search_fields = ['description']
    search_help_text = 'Поиск заказа'
    # actions = [reset_quantity]

    fields = ['customer', 'orders', 'order_price', 'date_added_order']
    readonly_fields = ['date_added_order']


admin.site.register(Order, OrderAdmin)
