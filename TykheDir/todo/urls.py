from django.urls import path
from . import views

urlpatterns = [

    path('', views.listTodo, name='listTodo'),
    path('create/', views.createTodo, name="createTodo"),
    path('<int:todo_pk>/deleteTodo', views.deleteTodo, name="deleteTodo"),

]