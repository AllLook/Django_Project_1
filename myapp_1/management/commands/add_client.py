from datetime import datetime

from django.core.management.base import BaseCommand

from myapp_1.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def handle(self, *args, **kwargs):
        client = Client(name='john conor', email='Judgment_Day@mail.com', telephone=000000000, address='Los Angeles',
                        registration_date=datetime.now())

        client.save()
        self.stdout.write(f'{client}')
