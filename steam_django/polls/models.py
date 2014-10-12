import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    app_ID = models.IntegerField(default=000000)
    price = models.IntegerField(default=0)
    description = models.CharField(default = "None", max_length = 1000)
    name = models.CharField(default = "None", max_length = 100)
    #tags=models.TextField(default="none", max_length=1000)
    def __str__(self):
        return str(self.app_ID)

class Achievement(models.Model):
    name=models.TextField(default="none", max_length=1000)
    appID=models.IntegerField(default=1)
    description=models.TextField(default="none", max_length=1000)
    globalAP= models.DecimalField(default=0.00, max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('name', 'appID')


class Player(models.Model):
    friends=models.TextField(default="none", max_length=1000)
    lastOnline=models.DateTimeField(default=0)
    activityState=models.IntegerField(default=1)
    steamID=models.IntegerField(default=1)
    steamID.primary_key=True
    displayName=models.TextField(default="none", max_length=1000)
    profileURL=models.TextField(default="none", max_length=1000)
    avatar=models.TextField(default="none", max_length=1000)
    visibilityState=models.IntegerField(default=1)


class Achieved(models.Model):
    steamID=models.IntegerField(default=1)
    name=models.TextField(default="none", max_length=1000)

class Owns(models.Model):
    totalPlaytime=models.IntegerField(default=1)
    recentlyPlaced=models.IntegerField(default=1)
    appID=models.IntegerField(default=1)
    steamID=models.IntegerField(default=1)

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
       return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        '''