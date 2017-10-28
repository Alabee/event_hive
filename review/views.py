from django.shortcuts import render, render_to_response
from event_details.models import Event_details

# Create your views here.
def index(request):
	return render_to_response('review/review.html', {'content': Event_details.objects.all()})

def art(request):
	return render_to_response('review/art.html', {'content': Event_details.objects.all()})

def partying(request):
	return render_to_response('review/partying.html', {'content': Event_details.objects.all()})

def conferences(request):
	return render_to_response('review/conferences.html', {'content': Event_details.objects.all()})

def tech(request):
	return render_to_response('review/tech.html', {'content': Event_details.objects.all()})
