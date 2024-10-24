from django.db import models

# Create your models here.
class Kgn(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(default='Cool')

class book(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(default='Cool')

class author(models.Model):
    title = models.CharField(max_length=120)
    # price = models.DecimalField(max_digits=10000, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    authored_books = models.TextField(default='Harry Potter')