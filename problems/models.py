from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Problem(models.Model):
    title = models.TextField(default=None, null=True)
    parent = models.IntegerField(default=0)
    created_by = models.ForeignKey("Mapuser", on_delete=models.CASCADE, blank=True, null=True, related_name = "mapuser")
    required_funding = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title




class Mapuser(AbstractUser):
    tokens = models.IntegerField(default=0)
