from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Peer(models.Model):
    user = models.OneToOneField(User)
    url = models.CharField(max_length=100)
