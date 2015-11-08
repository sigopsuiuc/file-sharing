from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Peer(models.Model):
    user = models.OneToOneField(User)
    url = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username


class PeerGroup(models.Model):
    groupname = models.CharField(max_length=32)
    peers = models.ManyToManyField(Peer) 
    def __str__(self):
        return self.groupname
