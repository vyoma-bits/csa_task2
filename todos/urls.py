from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'todos'  # Define the namespace for this app

urlpatterns = [
    path('', views.getAllTodos, name='get_todos'),
    path('<int:id>/', views.getTodo, name='get_todo_by_id'),
    path('create/', views.create, name='create_todo'),
    path('<int:id>/update/', views.update, name='update_todo'),
    path('<int:id>/delete/', views.delete, name='delete_todo'),
]
