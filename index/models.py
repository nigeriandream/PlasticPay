from django.db import models
import shortuuid
from django.db.models.signal import pre_save
from django.dispatch import receiver

# Create your models here.
# Admin model
class Admin(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    wallet_address = models.CharField(max_length=100)

    def __str__(self):
        return self.username

#  User model
class User(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    wallet_address = models.CharField(max_length=100)
    unique_number = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.username
    
    @receiver(pre_save, sender=User)
    def generate_unique_number(sender, instance, **kwargs):
        #only generate random number if it doesn't exist
        if not instance.unique_number:
            unique_number = shortuuid.uuid()[:12]
            instance.unique_number = unique_number

# register the signal receiver function
pre_save.connect(generate_unique_number, sender=User)

