from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path(
        '<int:article_pk>/comments/<int:comment_pk>/delete/',
        views.comment_delete,
        name='comment_delete',
    ),
    path('<int:article_pk>/emotes/<int:emotion>/', views.emotes, name='emotes'),
    path('<int:article_pk>/comment_emotes/<int:comment_pk>/<int:comment_emotion>/', views.comment_emotes, name='comment_emotes'),
]
