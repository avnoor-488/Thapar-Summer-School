from django.db import models
# from phonenumber_field import PhoneNumberField
from django.core.validators import FileExtensionValidator

# Create your models here.
class userData(models.Model):
    upper_limit = models.IntegerField()
    lower_limit = models.IntegerField()  
    doc = models.FileField(validators=[FileExtensionValidator( ['csv'] ) ])
    email = models.EmailField(default=None)
    # def __str__(self):
    #     return self.title   