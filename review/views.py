from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
	return render_to_response('review/review.html')

def art(request):
	return render_to_response('review/review.html')

def partying(request):
	return render_to_response('review/review.html')

def conferences(request):
	return render_to_response('review/review.html')

def tech(request):
	return render_to_response('review/review.html')

