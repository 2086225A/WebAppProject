from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, date

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profilepic = models.ImageField(upload_to='profile_images', blank=True) 

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.user.username

class Creation(models.Model):
    user = models.ForeignKey(User)
    imageID = models.CharField(max_length=5, unique=True)
    picture = models.ImageField(upload_to='', blank=True)
    likes = models.IntegerField(default=0)
    creationDate = models.DateTimeField("Date Published", default=datetime.now())

    def __unicode__(self):
        return self.imageID


class Rating(models.Model):
     #whats needed
    user = models.ForeignKey(User)
    imageID = models.ForeignKey(Creation)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.user.username

