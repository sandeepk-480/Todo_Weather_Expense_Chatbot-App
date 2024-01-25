from django.urls import path
from todo import views


urlpatterns = [
    path('', views.todoView, name='todo'),
    path('add/', views.add_data, name='add'),
    path('delete/<int:pk>/', views.delete_data, name='delete_todo'),
    path('finish/<int:pk>/', views.finish, name='finish'),
]

