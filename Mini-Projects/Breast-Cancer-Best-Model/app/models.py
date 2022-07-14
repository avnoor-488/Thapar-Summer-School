from django.db import models

# Create your models here.

from django.core.validators import FileExtensionValidator

# Create your models here.
class userData(models.Model):
    description = models.TextField()
    doc = models.FileField(validators=[FileExtensionValidator( ['csv'] ) ])
    email = models.EmailField(default=None)
    dummy = models.TextField()
    # def __str__(self):
    #     return self.title   
