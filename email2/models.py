from django.db import models

# Create your models here.
class Sendemail(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	description=models.TextField()
	def __str__(self):
		return self.name