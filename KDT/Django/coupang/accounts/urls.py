from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('mypage/<int:pk>/', views.mypage, name='mypage'),
]
