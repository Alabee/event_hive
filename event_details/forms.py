from django import forms

class Event_details_form(forms.Form):
	event_category= forms.CharField(max_length=2)
	event_name= forms.CharField(max_length = 255)
	event_description= forms.CharField(max_length = 1000)
	event_charges=forms.CharField(max_length = 255)