from django.urls import path
from . import views

app_name = 'number'
urlpatterns = [
    path('number/<int:number>/', views.number_print, name = 'number')
]
