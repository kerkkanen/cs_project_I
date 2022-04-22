from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    hearts = models.IntegerField()


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reciever')
    content = models.CharField(max_length=1000)