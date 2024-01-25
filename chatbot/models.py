from django.db import models

class ChatMessage(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()