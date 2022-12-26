from django.db import models

class StockQualityLabel(models.Model):
    trade_date = models.CharField(max_length=200)
    ts_code = models.CharField(max_length=200,primary_key=True)
    close = models.DecimalField(max_digits=10,decimal_places=2)
    next_day_close = models.DecimalField(max_digits=10, decimal_places=2)
    next_2day_close = models.DecimalField(max_digits=10, decimal_places=2)
    next_5day_close = models.DecimalField(max_digits=10, decimal_places=2)
    next_10day_close = models.DecimalField(max_digits=10, decimal_places=2)
    next_20day_close = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        unique_together = ("ts_code", "trade_date")

# Create your models here.
class StockDailyBasic(models.Model):
    trade_date = models.CharField(max_length=200)
    ts_code = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    stock_quality_label = models.OneToOneField(StockQualityLabel,on_delete=models.CASCADE, null=True)
    class Meta:
        unique_together = ("ts_code", "trade_date")



