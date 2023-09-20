from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from common.models import BaseModel





class CustomUser(AbstractUser):

    email_address_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Profile(BaseModel):
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

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)

class Pond(BaseModel):
    '''Pond types'''
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ponds')

    def __str__(self):
        return self.name



# Create your models here.
class StockingDensity(BaseModel):
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    to_stock = models.FloatField()
    verdict = models.TextField(null=True, blank=True)
    twenty_percent_decrease = models.FloatField()
    thirty_percent_decrease = models.FloatField()


    class Meta:
        ordering = ['-date_added']
        verbose_name = 'stocking density'
        verbose_name_plural = 'stocking densities'

    def __str__(self):
        return f"{self.length} by {self.width} by {self.height}"



