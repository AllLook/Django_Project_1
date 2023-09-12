from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('order_date/', views.client_order_date, name='order_date'),
    path('add_user/', views.user_form, name='user_form')
]
