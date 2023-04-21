from django.urls import path

from . import views

app_name='games'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/like/', views.like, name='like'),
    path('<int:post_pk>/answer/<str:answer>/', views.answer, name='answer'),
    path('<int:post_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
