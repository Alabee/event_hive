from django.shortcuts import render, render_to_response
from event_details.models import Event_details

# Create your views here.
def index(request):
	#if request.method =='GET':
		#search_query = request.GET.get('search_box')

	page = 'content'
	return render_to_response('review/review.html', {'category': page,'content': Event_details.objects.all()})

def art(request):
	page = 'content_art'
	return render_to_response('review/review.html', {'category': page,'content': Event_details.objects.filter(event_category='ART')})

def partying(request):
	page = 'content_partying'
	return render_to_response('review/review.html', {'category': page,'content': Event_details.objects.filter(event_category='P&C')})


def conferences(request):
	page = 'content_conferences'
	return render_to_response('review/review.html', {'category': page,'content': Event_details.objects.filter(event_category='C&T')})


def tech(request):
	page = 'content_tech'
	return render_to_response('review/review.html', {'category': page,'content': Event_details.objects.filter(event_category='TEC')})

#def search(request);
	#page = 'content_tech'
	#return render_to_response('review/review.html', {'category': page,'content': Event_details.objects.all()})	
