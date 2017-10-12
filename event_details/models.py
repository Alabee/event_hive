from django.db import models

# Create your models here.
class Details(models.Model):
	event_name = models.CharField(max_length = 255)

