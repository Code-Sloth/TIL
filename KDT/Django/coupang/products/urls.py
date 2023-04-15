from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:product_pk>/', views.detail, name='detail'),
    path('<int:product_pk>/delete/', views.delete, name='delete'),
    path('<int:product_pk>/update/', views.update, name='update'),
    path('<int:product_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:product_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('likes/<int:product_pk>/', views.likes, name='likes'),
]
