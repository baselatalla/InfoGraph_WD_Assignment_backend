from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=64,unique=True)
    photo_ppoi = PPOIField()
    photo = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='photo_ppoi'
    )
    email = models.EmailField(_('email address'))
    

    def __str__(self):
        return self.username


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name

class Maintenance_request(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE) 
    vehicle_name = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    status = models.CharField(max_length=64, default='Pending')
    image = models.ManyToManyField('ANYVEHICLE.Image', related_name='maintenance_requsets')
    discerption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.id}-{self.vehicle_name}'

