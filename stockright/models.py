from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token





class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=True)
    email_address_verified = models.BooleanField(default=False)
    

class Pond(models.Model):
    '''Pond types'''
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ponds')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_added = datetime.datetime.now(tz=timezone.utc)
        self.date_modified = datetime.datetime.now(tz=timezone.utc)
        return super(Pond, self).save(*args, **kwargs)


# Create your models here.
class StockingDensity(models.Model):
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    to_stock = models.FloatField()
    verdict = models.TextField(null=True, blank=True)
    twenty_percent_decrease = models.FloatField()
    thirty_percent_decrease = models.FloatField()
    date_checked = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_checked']
        verbose_name = 'stocking density'
        verbose_name_plural = 'stocking densities'

    def __str__(self):
        return f"{self.length} by {self.width} by {self.height}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_checked = datetime.datetime.now(tz=timezone.utc)
        self.date_modified = datetime.datetime.now(tz=timezone.utc)
        return super(StockingDensity, self).save(*args, **kwargs)


#generate and save token for a user
@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token=Token.objects.create(user=instance)
        token.save()