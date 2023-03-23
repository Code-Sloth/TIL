from django.urls import path
from . import views

app_name = 'calculate'
urlpatterns = [
    path('calculate/<int:number1>/<int:number2>/', views.calculate, name = 'calculate'),
    path('throw/', views.throw, name='throw'),
]
