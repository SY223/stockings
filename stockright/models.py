from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Pond(models.Model):
    '''Pond types'''
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

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
    twenty_percent_decrease = models.FloatField(null=True, blank=True)
    thirty_percent_decrease = models.FloatField(null=True, blank=True)
    date_checked = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_checked']
        verbose_name = 'stocking density'
        verbose_name_plural = 'stocking densities'

    def __str__(self):
        return f"{self.length} by {self.width} by {self.height}"
