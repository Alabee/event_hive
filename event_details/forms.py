from django import forms

class Event_details_form(forms.Form):
	event_category= forms.CharField(max_length=2)
	event_name= forms.CharField(max_length = 255)
	event_description= forms.Textarea()
	event_charges=forms.CharField(max_length = 255)
	event_date = forms.DateField()