from tkinter import CASCADE
from django.db import models


class Account(models.Model):
    Username = models.CharField(max_length=20, unique=True)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Username


class Ship(models.Model):
    ship_name = models.CharField(max_length=30)
    ship_owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    fuel = models.BigIntegerField()
    max_fuel = models.BigIntegerField()

    def level(self):
        return self.fuel/self.max_fuel*100

    def __str__(self):
        return self.ship_name
