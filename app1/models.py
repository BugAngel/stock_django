from django.db import models


# Create your models here.
class StockDailyBasic(models.Model):
    ts_code = models.CharField(max_length=200,primary_key=True)
    symbol = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    trade_date = models.CharField(max_length=200)
