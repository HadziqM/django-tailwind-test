from django.db import models


class Account(models.Model):
    Username = models.CharField(max_length=20, unique=True)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Username
