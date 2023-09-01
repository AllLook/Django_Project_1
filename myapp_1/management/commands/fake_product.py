from datetime import datetime

from django.core.management.base import BaseCommand
from myapp_1.models import Product


class Command(BaseCommand):
    help = 'Generate product'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='product')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'name{i}', price=100 + i, description=f'bldblabla + {i}', quantity=1,
                              date_added_product=datetime.now())
            product.save()
            self.stdout.write(f'{product}')
