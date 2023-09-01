from datetime import datetime

from django.core.management.base import BaseCommand
from myapp_1.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Create order'

    def handle(self, *args, **kwargs):
        i = 1
        while i < 10:
            for client in Client.objects.all():
                order = Order(customer=client, orders=Product.objects.filter(name=f'name{i}').first(),
                              order_price=100,
                              date_added_order=datetime.now())
                order.save()
                print(order)
                i += 1
