from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.db.models import get_model

from django import forms
from .models import Brewery, BrewPub, Beer, Bar, Announcments

def home(request):

	content = Announcments.objects.filter(-'pub_date')
	context = {"content":content}
	return render(request, 'base.html', context)

def contact(request):

def index(request):
	cases = {
		'Brewery':Brewery.objects.all(),
		'Brewpub':BrewPub.objects.all(),
		'Bar':Bar.objects.all(),
		'Beer':Beer.objects.all(),
		'Announcments':Announcments.objects.all(),
		}
	#ajax searching
	if request.is_ajax():
		mimetype = 'application/json'
		try:
			#search term
			q = request.GET.get('q')
			#category to search
			s = request.GET.get('s')

		except KeyError:
			html = {'results': "error!"}
			data = {'html':html}
			return HttpResponse(simplejson.dumps(data), mimetype)

		if (q is not None) and (s is not None):
			results = {}
			if s == "all":
				for i in cases:
					#change someapp!!!
					model = get_model('someapp', i)
					results += model.objects.filter(title__icontains=q)
			else:
				try:
					model = get_model('someapp', s)
					results = model.objects.filter(title__icontains=q)
				except:
					results = "whoops, couldnt find model with s parameter"
			html = render_to_string('index.html', {'results':results})
			data = {'html', html}
			return HttpResponse(simplejson.dumps(data), mimetype)

		else:
			html = "error!"
			data = {'html':html}
			return HttpResponse(simplejson.dumps(data), mimetype)

			#regular view:
	elif not request.GET.get('s', None):
		#return render("no subject!.. How'd you get here?")

	else:
		subject = request.GET.get('s', None)
		model = get_model('someapp', s)
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