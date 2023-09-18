from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.conf import settings





class CustomUser(AbstractUser):
    email_address_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_added = datetime.datetime.now(tz=timezone.utc)
        self.date_modified = datetime.datetime.now(tz=timezone.utc)
        return super(Profile, self).save(*args, **kwargs)

    

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
    date_added = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_added']
        verbose_name = 'stocking density'
        verbose_name_plural = 'stocking densities'

    def __str__(self):
        return f"{self.length} by {self.width} by {self.height}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_added = datetime.datetime.now(tz=timezone.utc)
        self.date_modified = datetime.datetime.now(tz=timezone.utc)
        return super(StockingDensity, self).save(*args, **kwargs)


