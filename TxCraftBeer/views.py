from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.db.models import get_model
from django.http import Http404, HttpResponse
from django.contrib.contenttypes.models import ContentType
#from django.core import serializers


from .forms import Contact
from .models import Brewery, BrewPub, Beer, Bar, Announcement, Contact, Image, Video

cases = ['Brewery','Brewpub','Bar','Beer','Announcement']

### Helper functions ###
def _json_response(context):
	return HttpResponse(json.dumps(context), mimetype="application/json")

def findAll(query):
	cases = ['Brewery','Brewpub','Bar','Beer','Announcement']
	results = {}
	subject = []
	errors = []
	resultlength =0
	for obj in cases:
		try:
			subject.append(obj)
			model = get_model('TxCraftBeer', obj)
			if model.objects.filter(name__icontains=query):
				new = (model.objects.filter(name__icontains=query).order_by('name'))
				results[obj] =new
				resultlength += new.count()
		except Exception as e:
			errors.append(e)
	return {'results':results,
			'query':query, 
			'errors':errors, 
			'subject':subject, 
			'length':resultlength}

### Views ###
def landing(request):
	##should find a different way to find random images..
	## ordering every image will be ineffecient when db grows
	image = Image.objects.order_by('?')[0]
	context = {"image":image,}
	return render(request, 'landing.html', context)

def home(request):
	content=None
	errors=None
	try:
		content = Announcement.objects.order_by('-pk')[0:4]
	except Exception as e:
		errors = e

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
		if s == 'all':
			context= findAll(q)
			if request.is_ajax():
				_json_response(context)
			return render(request, 'index.html', context)
		try:
			model = get_model('TxCraftBeer', s)
			results = model.objects.filter(name__icontains=q)
			resultlength = results.count()

			if request.is_ajax():
				context = {'results':results,'subject':s,'query':q,"length":resultlength}
				_json_response(context)

			#regular index
			else:
				context = {'results':results,'subject':s,'query':q,"length":resultlength}
				return render(request, 'index.html', context)

			#getting model doesnt work
		except Exception as e:
			errors = e
			return render(request, 'index.html', {'errors':errors})

		### if no subject, search everything
	elif not request.GET.get('s', None) and request.GET.get('q',None):
		q = request.GET.get('q', None)
		try:
			context= findAll(q)
			if request.is_ajax():
				_json_response(context)
			return render(request, 'index.html', context)

		except Exception as e:
			context={'errors':e}
			return render(request, 'index.html', context)

		##no query.. how'd you get here?
	else:
		if request.GET.get('q',None) == '':
			error = ["no query!",]
			context = {'errors':error}
			return render(request, 'index.html', context)
		else:
			error = ["how'd you get here?",]
			context = {'errors':error}
			return render(request, 'index.html', context)


#### Specific views ######
def contentHome(request, subject, region=None):
	if region:
		try:
			model = get_model('TxCraftBeer', subject)
			topresults = model.objects.filter(region__icontains=region)[0:4]
		except Exception as e:
			error = [e,"it got a region but failed!"]
			return render(request, '404.html', {'error':error, 'subject':subject})
	else:
		try:
			model = get_model('TxCraftBeer', subject)
			topresults = model.objects.order_by('-pk')[0:4]
		except Exception as e:
			error = [e,"it didnt get a region!"]
			return render(request, '404.html', {'error':error})
	vid = "videos/"+subject+"/home.mp4"
	context = {'results':topresults, 'vid':vid, 'subject':subject}
	return render(request, 'contentHome.html', context)

def contentProfile(request, subject, id):
	errors = []
	try:
		model = get_model('TxCraftBeer', subject)
		result = model.objects.get(id=id)
		try:
			beers = result.beer_set.all()
			bars = None
		except AttributeError as e:
			#if error, it must be beer.
			errors.append('we couldnt get beer_set: {0}'.format(e))
			beers = None
			try:
				bars = result.bar.all()
			except Exception as e:
				errors.append("it screwed up again: {0}".format(e))
				context = {'errors': errors}
				return render(request, 'contentProfile.html', context)

		try:
			content = ContentType.objects.get_for_model(result)
			pics = Image.objects.filter(content_type=content, object_id=result.id)
		except Image.DoesNotExist:
			pics="does not exist!"
		except Exception as e:
			pics = e
		try:
			content = ContentType.objects.get_for_model(result)
			video = Video.objects.filter(content_type=content, object_id=result.id)
		except Video.DoesNotExist:
			video="does not exist!"
		except Exception as e:
			video=e

		context = {
		'errors':errors,
		'beers':beers,
		'pics':pics,
		'video':video, 
		'bars':bars
		}
		return render(request, 'contentProfile.html', context)
	except Exception as e:
		errors.append('FAILURE!: {0}'.format(e))
		context = {'errors': errors}
		return render(request, 'contentProfile.html', context)



###       ADMIN VIEWS      ###

def admin_home(request):
	return HttpResponse('Under Construction')