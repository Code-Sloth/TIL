from django.urls import path
from articles import views

app_name='articles'
urlpatterns = [
    path('api/v1/', views.article_list, name='article_list'),
    path('api/v1/<int:article_pk>/', views.article_detail, name='article_detail'),
    path('', views.index, name='index'),
]
