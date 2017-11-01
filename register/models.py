from django.db import models

# Create your models here.
class User_detail(models.Model):
	name = models.CharField(max_length = 500)
	email =  models.CharField(max_length = 500)
	phone = models.CharField(max_length = 250)

	def __str__(self):
		return self.name

