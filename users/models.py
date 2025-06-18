from django.db import models
from django.contrib.auth.models import AbstractUser


#custom user
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.username

# Telegram user
class TelegramUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True , unique= True)
    username = models.CharField(max_length=150, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"{self.username} -> {self.user_id}"





