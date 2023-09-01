from django.db import models

from django.db import models
from datetime import datetime


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    telephone = models.IntegerField()
    address = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Client: {self.name}, email:{self.email}, telephone: {self.telephone}, address: {self.address}, registration date{self.registration_date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    date_added_product = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, description: {self.description}, quantity of goods: {self.quantity}, date added: {self.date_added_product}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    orders = models.OneToOneField(Product, on_delete=models.CASCADE, default=None)
    order_price = models.DecimalField(max_digits=16, decimal_places=2)
    date_added_order = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order: customer: {self.customer}, orders: {self.orders}, order price: {self.order_price}, date added order: {self.date_added_order}'
