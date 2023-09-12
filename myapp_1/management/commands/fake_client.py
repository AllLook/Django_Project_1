from datetime import datetime

from django.core.management.base import BaseCommand
from myapp_1.models import Client


class Command(BaseCommand):
    help = 'Generate client'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client id')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'name{i}', email=f'name{i}@mail{i}.com', telephone=000000 + i,
                            address=f'LosAngeles,{i}', registration_date=datetime.now(), age=0 + i,
                            about_me=f'aaaaa{i}', password=f'11111{i}', user_photo=None)
            client.save()
            self.stdout.write(f'{client}')
