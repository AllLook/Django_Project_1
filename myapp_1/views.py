from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from datetime import datetime
from myapp_1.models import Client, Order

logger = logging.getLogger(__name__)

text_1 = """ 
<h1>A little about myself</h1>
<p>Hello! My name is Alexey and I am a beginner developer.</p>
"""

text_2 = """ 
<h1>A little about my application</h1>
<p>This is my first Django app, but it works!</p>
"""


def index(request):
    logger.info(f'Страница index вызвана {datetime.now()}')
    return render(request, 'base.html')


def about(request):
    logger.info(f'Страница about вызвана {datetime.now()}')
    return HttpResponse(text_2)


def client_order(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    order = Order.object.filter(client=client).order_by('')