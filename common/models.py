from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class BaseModel(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_added = datetime.datetime.now(tz=timezone.utc)
        self.date_modified = datetime.datetime.now(tz=timezone.utc)
        return super().save(*args, **kwargs)
    
    class Meta:
        abstract = True