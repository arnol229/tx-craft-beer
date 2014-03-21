from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

from django import forms
from .models import Brewery, BrewPub, Beer, Bar, Announcments

def home(request):
	
	content = Announcments.objects.filter(-'pub_date')
	return render(request, 'base.html', content)

def contact(request):

def index(request):
	#ajax searching
	if request.is_ajax():
		try:
			#search term
			q = request.GET.get('q')
			#category to search
			s = request.GET.get('s')
		except KeyError:
			data = {'results': "error!"}
			return render_to_response('index', data, context_instance=RequestContext(request))

		if (q is not None) and (s is not None):
			results = s.objects.filter(title__icontains=q)# can an object be referenced like this?
			data = {'results':results}
			return render_to_response('index.html', data, context_instance=RequestContext(request))

	elif not request.GET.get('s', None):
		#return render("no subject!.. How'd you get here?")

	else:
		subject = request.GET.get('s', None)

		cases = {
		'Brewery':Brewery.objects.all(),
		'Brewpub':BrewPub.objects.all(),
		'Bar':Bar.objects.all(),
		'Beer':Beer.objects.all(),
		'Announcments':Announcments.objects.all(),
		}

		try:
			results = cases[subject]
		except KeyError:
			results = cases

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