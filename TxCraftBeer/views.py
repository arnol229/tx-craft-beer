from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.db.models import get_model

from django import forms
from .models import Brewery, BrewPub, Beer, Bar, Announcments

def _jason_response(context):
	return HttpResponse(json.dumps(context), mimetype="application/json")

def findAll(query):
	cases = ['Brewery','Brewpub','Bar','Beer','Announcments']
	results = []
	errors = []
	context = {}
	for obj in cases:
		model = get_model('TxCraftBeer', obj)
		try:
			results += model.objects.order_by('-pk').filter(title__icontains=q)[0:2]
		except Exception as e:
			errors += e
	context = {'results':results, 'errors':errors, 'query':query, 'errors':errors}
	return context

def home(request):
	content=None
	errors=None
	try:
		content = Announcments.objects.order_by('-pk')[0:4]
	except Exception as e:
		errors = str(e)

	context = {"content":content, "errors":errors}
	return render(request, 'base.html', context)

#def contact(request):
#

#this will prolly get deleted.
#def search(request):
#
#	cases = {
#	'Brewery':Brewery.objects.all(),
#	'Brewpub':BrewPub.objects.all(),
#	'Bar':Bar.objects.all(),
#	'Beer':Beer.objects.all(),
#	'Announcments':Announcments.objects.all(),
	#}

	#if request.is_ajax():
	#	if request.method == "GET":
	#		mimetype = 'application/json'
	#		try:
	#			#search term
	#			q = request.GET.get('q')
	#			#category to search
	#			s = request.GET.get('s')
	#
	#		except KeyError:
	#			html = {'results': "error! Couldn't pull query or subject from request!"}
	#			data = {'html':html}
	#			return HttpResponse(simplejson.dumps(data), mimetype)
	#
	#		if (q is not None) and (s is not None):
	#			results = {}
	#			if s == "all":
	#				for i in cases:
	#					#change someapp!!!
	#					model = get_model('TxCraftBeer', i)
	#					results += model.objects.filter(title__icontains=q)
	#			else:
	#				try:
	#					model = get_model('TxCraftBeer', s)
	#					results = model.objects.filter(title__icontains=q)
	#				except:
	#					results = "whoops, couldnt find model with s parameter"
	#			html = render_to_string('index.html', {'results':results})
	#			data = {'html', html}
	#			return HttpResponse(simplejson.dumps(data), mimetype)
	#
	#		else:
	#			html = "error!"
	#			data = {'html':html}
	#			return HttpResponse(simplejson.dumps(data), mimetype)

def index(request):
	context = {}
	if request.GET.get('s', None):
		s = request.GET.get('s', None)
		q = request.GET.get('q',None)

			#ajax search update and subject is all
		if s == "all" and request.is_ajax():
			try:
				context= findAll(q)
				_jason_response(context)
			except Exception as e:
				context={'results':e}
				_jason_response(context)

			#ajax search update and has a specific subject
		elif request.is_ajax():
			try:
				model = get_model('TxCraftBeer', s)
				results = model.objects.filter(title__icontains=q)
				context = {'results':results}
				_jason_response(context)
			except Exception as e:
				context ={'results':e}
				_jason_response(context)

			#Not ajax, regular index
		else:
			if s == 'all':#not recognizing s=all parameter
				context = findAll(q)
				return render(request, 'index.html',context)
			else:
				try:
					model = get_model('TxCraftBeer', s)
					if not model:
						results="no model haha"
					else:
						results = model.objects.filter(title__icontains=q)
				except Exception as e:
					results = e

		context = {'results':results, "query":q, "subject":s}

		return render(request, 'index.html', context)

	else:
		context = {'results':"no subject! wtf?!"}
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