from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=20);
    age = models.IntegerField();
    mobile = models.BigIntegerField();
    email = models.EmailField();
    message = models.CharField(max_length=250)
