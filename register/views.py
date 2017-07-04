from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader

from register.models import User_details
from register.forms import User_details_form

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = User_details_form(request.POST)
		if form.is_valid():
			name = request.POST.get('name')
			email = request.POST.get('email')
			phone = request.POST.get('phone')

			details_obj = User_details(name = name, email = email, phone = phone)
			details_obj.save()

			return HttpResponse("<h2>Successfully registered</h2>")

	else:
		form = User_details_form()

	return render(request, 'register/register.html', {
		'form': form,
		})
