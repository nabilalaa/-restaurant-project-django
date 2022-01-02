from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True)
    category = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Calc(models.Model):
    name = models.CharField(max_length=100,null=True)
    # price = models.FloatField(null=True)
    total = models.FloatField(null=True)

    def __str__(self):
        return self.name

