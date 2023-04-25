from django.urls import path
from articles import views

app_name='articles'
urlpatterns = [
    path('api/v1/', views.article_list, name='article_list'),
    path('api/v1/<int:article_pk>/', views.article_detail, name='article_detail'),
    path('api/v1/comments/', views.comment_list, name='comment_detail'),
    path('api/v1/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('api/v1/<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('', views.index, name='index'),
]