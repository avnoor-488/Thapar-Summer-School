from django.db import models

# Create your models here.

from django.core.validators import FileExtensionValidator

# Create your models here.
class userData(models.Model):
    doc = models.FileField(validators=[FileExtensionValidator( ['csv'] ) ])
    email = models.EmailField(default=None)
