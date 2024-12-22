from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(default='default.png')
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



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

    class Meta:
        ordering = ['-updated', '-created', ]

    def __str__(self):
        return self.name

class Message(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', ]


    def __str__(self):
        return self.body[0:50]
