from django.core.management.base import BaseCommand

from myapp_1.models import Client


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserId delete')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        client.delete()
        self.stdout.write(f'Delete {client}')
