from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
]
