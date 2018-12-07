from django.db import models


# Create your models here.


class Description(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField(max_length= 1024)
	
	def __str__(self):
		return self.title