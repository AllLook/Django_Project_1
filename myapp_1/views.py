from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import datetime

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
    return HttpResponse(text_1)


def about(request):
    logger.info(f'Страница about вызвана {datetime.now()}')
    return HttpResponse(text_2)
