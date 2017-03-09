from django.db import models
from django.utils import timezone

# Create your models here.


class UserLoginForm(models.Model):
 	username = models.CharField(max_length=10,null=True)
 	mob_no = models.IntegerField(null=True)
 	email = models.TextField(null=True)
 	password = models.TextField(max_length=8,null=True)
 
 	def __unicode__(self):
		return str(self.username) 