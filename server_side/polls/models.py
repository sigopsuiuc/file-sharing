from django.db import models

# Create your models here.
#



#temporary class for peer list, there should be more secure and robust way to do this

class peer(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name



