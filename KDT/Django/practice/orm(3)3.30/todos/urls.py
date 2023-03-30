from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:delete_pk>/delete/', views.delete, name='delete'),
    path('<int:edit_pk>/edit/', views.edit, name='edit'),
    path('<int:update_pk>/update/', views.update, name='update'),
    path('<int:check_pk>/check/', views.check, name='check'),
]
