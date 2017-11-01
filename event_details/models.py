from django.db import models

# Create your models here.
class Event_details(models.Model):
	event_category = models.CharField(max_length=2)
	event_name = models.CharField(max_length = 255)
	event_description = models.TextField()
	event_charges = models.CharField(max_length = 255)
	event_date = models.DateField()

	def __str__(self):
		return self.name

'''
, choices=EVENT_CATEGORIES

	EVENT_CATEGORIES = (
		('ART', 'ART & PHOTOGRAPHY'),
		('P&C', 'PARTYING & CLUBBING'),
		('C&T', 'CONFERENCES & TALKS'),
		('TEC', 'E-WORLD'),
		)
'''