from django.shortcuts import render,render_to_response
from django.http import HttpResponse

from event_details.models import Event_details
from event_details.forms import Event_details_form

# Create your views here.
def index(request):
	return render_to_response('event_details/events.html', {'content': Event_details.objects.all()})

def event_details(request):
	if request.method == 'POST':
		form = Event_details_form(request.POST)
		if form.is_valid(): 
			event_category = request.POST.get('category')
			event_name= request.POST.get('event_name')
			event_description= request.POST.get('description')
			event_charges= request.POST.get('charges')
			event_date = request.POST.get('date')

			event_details = Event_details(event_category = event_category, event_name = event_name, event_description = event_description, event_charges = event_charges, event_date = date)
			event_details.save()

			return HttpResponse("<h2>Success</h2>")
	else:
		form = Event_details_form()

	return render(request, 'event_details/event_details_form.html', {
		'form': form,
		})