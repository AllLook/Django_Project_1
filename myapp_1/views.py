from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from datetime import datetime
from myapp_1.models import Client, Order
from datetime import *
from django.utils import timezone
from .form_user import UserForm

logger = logging.getLogger(__name__)

today = datetime.today()

text_1 = """ 
<h1>A little about myself</h1>
<p>Hello! My name is Alexey and I am a beginner developer.</p>
"""

text_2 = """ 
<h1>A little about my application</h1>
<p>This is my first Django app, but it works!</p>
"""


def in_7_days():
    return timezone.now() + timedelta(days=7)


def in_30_days():
    return timezone.now() + timedelta(days=30)


def in_366_days():
    return timezone.now() + timedelta(days=366)


def index(request):
    logger.info(f'Страница index вызвана {datetime.now()}')
    return render(request, 'myapp_1/base.html')


def about(request):
    logger.info(f'Страница about вызвана {datetime.now()}')
    return HttpResponse(text_2)


def client_order_date(request):
    orders = Order.objects.all()
    temp_orders7 = in_7_days()
    temp_orders30 = in_30_days()
    temp_orders366 = in_366_days()
    orders7 = Order.objects.filter(date_added_order__lte=temp_orders7)
    orders30 = Order.objects.filter(date_added_order__lte=temp_orders30)
    orders366 = Order.objects.filter(date_added_order__lte=temp_orders366)
    return render(request, 'myapp_1/all_orders_client.html',
                  {'orders': orders, 'orders7': orders7, 'orders30': orders30, 'orders366': orders366})


def user_form(request):
    message = ''
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            address = form.cleaned_data['telephone']
            age = form.cleaned_data['age']
            about_me = form.cleaned_data['about_me']
            password = form.cleaned_data['password']
            user_photo = form.cleaned_data['user_photo']
            fs = FileSystemStorage()
            if user_photo:

                user_photo = fs.save(user_photo.name, user_photo)
            else:
                user_photo = None
            client = Client(name=name, email=email, telephone=telephone, address=address, age=age, about_me=about_me,
                            password=password, user_photo=user_photo)
            client.save()
            message = 'User save'
    else:
        form = UserForm()
        message = 'Fill the form!'

    return render(request, 'myapp_1/add_user.html', {'form': form, 'message': message})
