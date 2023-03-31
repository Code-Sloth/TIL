from django.urls import path
from . import views

app_name = 'accountbooks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:books_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:books_pk>/edit/', views.edit, name='edit'),
    path('<int:books_pk>/update/', views.update, name='update'),
    path('<int:books_pk>/delete/', views.delete, name='delete'),
    path('<int:books_pk>/copy/', views.copy, name='copy'),
]
