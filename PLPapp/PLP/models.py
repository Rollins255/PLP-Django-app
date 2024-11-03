from django.db import models # type: ignore

# Create your models here.
models

class StockPurchase(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()

    def __str__(self):
        return self.item_name


class StockSale(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField()

    def __str__(self):
        return self.item_name