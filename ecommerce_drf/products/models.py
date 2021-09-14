from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=500)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    inventory_quantity = models.IntegerField(default=0.0)
    slug = models.SlugField(max_length=250, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    udapted_at = models.DateTimeField(auto_now=True)
