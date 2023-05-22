import uuid
from django.db import models


class Pond(models.Model):
    '''Pond types'''
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
class StockingDensity(models.Model):
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)
    length = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    to_stock = models.FloatField(null=True, blank=True)
    verdict = models.TextField(null=True, blank=True)
    date_checked = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_checked']
        verbose_name = 'stocking density'
        verbose_name_plural = 'stocking densities'

    def __str__(self):
        return f"{self.length} by {self.width} by {self.height}"
