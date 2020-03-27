from django.db import models
from .utils import create_shortcode
from django.core.validators import MinValueValidator,MaxValueValidator
#from django.contrib.auth import user
from django.conf import settings

class Database(models.Model):
    url=models.CharField(max_length=100)
    shortcode=models.CharField(max_length=20)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)


    def save(self,*args,**kwargs):
        self.shortcode=create_shortcode(self)
        super(Database,self).save(*args,**kwargs)


    def __str__(self):
        return self.url

   