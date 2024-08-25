from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.todo_delete, name='todo_delete'),
    path('completed/<int:id>/', views.todo_completed, name='todo_completed'),
]
