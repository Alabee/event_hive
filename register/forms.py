from django import forms

class User_details_form(forms.Form):
	name = forms.CharField(max_length = 500)
	email =  forms.CharField(max_length = 500)
	phone = forms.CharField(max_length = 250)

class Login_form(forms.Form):
	user_name = forms.CharField(max_length = 250)
	password = forms.CharField(max_length = 250)