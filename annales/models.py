from django.db import models

# Create your models here.

class Annale(models.Model): #Mathis stop les blagues nulles s'il te plait...
	title = models.CharField(max_length = 100)
	link = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.title
		