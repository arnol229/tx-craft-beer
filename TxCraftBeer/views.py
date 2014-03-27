from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.db.models import get_model

from django import forms
from .models import Brewery, BrewPub, Beer, Bar, Announcments


### Helper functions ###
def _jason_response(context):
	return HttpResponse(json.dumps(context), mimetype="application/json")

def findAll(query):
	cases = ['Brewery','Brewpub','Bar','Beer','Announcments']
	results = {}
	subject = []
	errors = []
	toptwo=[]
	context = {}
	for obj in cases:
		subject.append(obj)
		model = get_model('TxCraftBeer', obj)
		if model.objects.filter(name__icontains=query):
			new = {obj:model.objects.filter(name__icontains=query).order_by('name')}
			results.update(new)

	return {'results':results, 'query':query, 'errors':errors, 'subject':subject}

### Views ###
def home(request):
	content=None
	errors=None
	try:
		content = Announcments.objects.order_by('-pk')[0:4]
	except Exception as e:
		errors = str(e)

	context = {"content":content, "errors":errors}
	return render(request, 'base.html', context)

def index(request):
	context = {}
	##if subject, search it
	if request.GET.get('s', None) and request.GET.get('q',None):
		s = request.GET.get('s', None)
		q = request.GET.get('q',None)

		if request.is_ajax():
			try:
				model = get_model('TxCraftBeer', s)
				results = model.objects.filter(name__icontains=q)
				context = {'results':results}
				_jason_response(context)
			except Exception as e:
				context ={'results':e}
				_jason_response(context)

			#regular index
		else:
			try:
				model = get_model('TxCraftBeer', s)
				results = model.objects.filter(name__icontains=q)
			except Exception as e:
				results = e
			context = {'results':results,'subject':s,'query':q}
			return render(request, 'index.html', context)

		### if no subject, search everything
	elif not request.GET.get('s', None) and request.GET.get('q',None):
		q = request.GET.get('q', None)
		if request.is_ajax():
			try:
				context= findAll(q)
				_jason_response(context)
			except Exception as e:
				context={'results':e}
				_jason_response(context)
		else:
			context = findAll(q)
			return render(request, 'index.html',context)

		##no query.. how'd you get here?
	else:
		results = "how'd you get here?"
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