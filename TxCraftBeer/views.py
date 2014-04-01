from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.db.models import get_model
from django.http import Http404

from .forms import Contact
from .models import Brewery, BrewPub, Beer, Bar, Announcement, Contact

cases = ['Brewery','Brewpub','Bar','Beer','Announcement']

### Helper functions ###
def _json_response(context):
	return HttpResponse(json.dumps(context), mimetype="application/json")

def findAll(query):
	cases = ['Brewery','Brewpub','Bar','Beer','Announcement']
	results = {}
	subject = []
	errors = []
	toptwo=[]
	context = {}
	resultlength =0
	for obj in cases:
		try:
			subject.append(obj)
			model = get_model('TxCraftBeer', obj)
			if model.objects.filter(name__icontains=query):
				new = {obj:model.objects.filter(name__icontains=query).order_by('name')}
				results.update(new)
				resultlength += len(new.items()[0])
		except Exception as e:
			errors.append(e)
	return {'results':results, 'query':query, 'errors':errors, 'subject':subject, 'length':resultlength}

### Views ###
def home(request):
	content=None
	errors=None
	try:
		content = Announcement.objects.order_by('-pk')[0:4]
	except Exception as e:
		errors = str(e)

	context = {"content":content, "errors":errors}
	return render(request, 'base.html', context)

def contact(request):
	if request.method == 'POST':
		form = Contact(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			body = form.cleaned_data['body']
			sender = form.cleaned_data['sender']
			NewMessage = Contact(subject, body, sender)
			NewMessage.save()

			response = "Thanks for your input!"
			context = {'response':response}
			_json_response(context)
	else:
		form = Contact()
	return render(request, 'contact.html', {
		'form':form
		})



	return render(request, 'base.html', context)

def index(request):
	context = {}
	resultlength = 0
	##if subject, search it
	if request.GET.get('s', None) and request.GET.get('q',None):
		s = request.GET.get('s', None)
		q = request.GET.get('q',None)

		try:
			model = get_model('TxCraftBeer', s)
			results = model.objects.filter(name__icontains=q)
			resultlength = results.count()

			if request.is_ajax():
				try:
					context = {'results':results,'subject':s,'query':q,"length":resultlength}
					_json_response(context)
				except Exception as e:
					context ={'results':e}
					_json_response(context)

			#regular index
			else:
				context = {'results':results,'subject':s,'query':q,"length":resultlength}
				return render(request, 'index.html', context)

			#getting model doesnt work
		except Exception as e:
			results = e

		### if no subject, search everything
	elif not request.GET.get('s', None) and request.GET.get('q',None):
		q = request.GET.get('q', None)
		try:
			context= findAll(q)
			if request.is_ajax():
				_json_response(context)
			return render(request, 'index.html', context)

		except Exception as e:
			context={'results':e}
			return render(request, 'index.html', context)

		##no query.. how'd you get here?
	else:
		results = "how'd you get here?"
		context = {'results':results}
		return render(request, 'index.html', context)


#### Specific views ######
def contentHome(request, subject, region = None):
	if region:
		try:
			model = get_model('TxCraftBeer', subject)
			topresults = model.objects.filter(region__icontains=region)[0:4]
		except Exception as e:
			error = e
			return render(request, '404.html', {'error':error})
	else:
		try:
			model = get_model('TxCraftBeer', subject)
			topresults = model.objects.order_by('-pk')[0:4]
		except Exception as e:
			error = e
			return render(request, '404.html', {'error':error})
	
	context = {'results':topresults}
	return render(request, 'contentHome.html', context)

def contentProfile(request, subject, id):
	try:
		model = get_model('TxCraftBeer', subject)
		result = model.objects.filter(id=id)
		context = {'result':result}
		return render(request, 'contentProfile.html', context)
	except Exception as e:
		context = {'result': e}
		return render(request, 'contentProfile.html', context)