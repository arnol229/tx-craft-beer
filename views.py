from django.shortcuts import render
from django import forms
from .models import Brewery, BrewPub, Beer, Bar, Announcments

def home(request):

def contact(request):

def index(request, subject):
	#list all of a type (brewery, brewpub, etc)
	#can subject be a search?
	if not subject:
		#return render(no subject!)

	elif subject != 'Brewery' or 'Brewpub' or 'Bar' or 'Beer' or 'Announcments':
		#return render(its not valid!)
		#or assume it is a search term?
	else:
		cases = {
		'Brewery':Brewery.objects.all(),
		'Brewpub':BrewPub.objects.all(),
		'Bar':Bar.objects.all(),
		'Beer':Beer.objects.all(),
		'Announcments':Announcments.objects.all(),
		}
		results = cases[subject]

		context = {'results':results}

		return render(request, 'index.html', context)


#### Specific views ######
def brewery(request, id):
	result = Brewery.objects.filter(id=id)
	context = {'result':result}
	return render(request, 'brewery.html', context)

def brewpub(request, id):
	result = BrewPub.objects.filter(id=id)
	context = {'result':result}
	return render(request, 'brewpub.html', context)

def bar(request, id):
	result = Bar.objects.filter(id=id)
	context = {'result':result}
	return render(request, 'bar.html', context)

def beer(request, id):
	result = Beer.objects.filter(id=id)
	context = {'result':result}
	return render(request, 'beer.html', context)