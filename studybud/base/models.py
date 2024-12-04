from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
# Create your models here.

class Topic(Model):
    name = models.CharField(max_length=200, blank=False, null= False)

    def __str__(self):
        return self.name
    

class Room(Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null= True )
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description= models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Message(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]
