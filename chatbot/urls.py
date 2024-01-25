from django.urls import path
from chatbot import views


urlpatterns = [
    path('', views.chatbotView, name='chatbot'),
    path('del/<int:pk>/', views.del_chat, name='delete_chat'),
]

