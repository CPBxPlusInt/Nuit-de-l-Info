from django.db import models

# Create your models here.
 
class Event(models.Model):
	title = models.CharField(max_length = 150)
	description = models.TextField(max_length = 512)
	lieu = models.CharField(max_length = 150)
	map = models.CharField(max_length = 200)
	date = models.DateField()
	heure = models.TimeField()
	
	def __str__(self):
		preview = '{0} {1} {2}'.format(self.lieu, self.date, self.heure)
		return preview