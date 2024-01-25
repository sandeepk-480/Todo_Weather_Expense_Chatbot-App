from django.urls import path
from expense import views


urlpatterns = [
    path('', views.expenseView, name='expense'),
    path('add/', views.add_expense, name='add_expense'),
    path('delete/<int:pk>/', views.delete, name='delete_expense'),
]

