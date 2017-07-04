from django.db import models

# Create your models here.
class Details(models.Model):
	event_category = models.CharField(max_length = 250)
	event_name = models.CharField(max_length = 250)
	event_image1 = models.CharField(max_length = 1000)
	event_image2 = models.CharField(max_length = 1000)
	event_image3 = models.CharField(max_length = 1000)
	event_description = models.TextField()
	event_amount = models.CharField(max_length = 1000)
	event_location = models.CharField(max_length = 1000)
	event_date = models.DateTimeField()

