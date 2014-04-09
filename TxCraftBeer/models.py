from django.db import models
from django.db.models import get_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.forms.fields import ChoiceField
import os
import datetime

class Brewery(models.Model):
	name=models.CharField(max_length=20)
	address=models.CharField(max_length=50)
	bio = models.CharField(max_length=500)
	region = models.CharField(max_length=20)

	class Meta:
		ordering = ['name']
		verbose_name_plural = "Breweries"
	def __unicode__(self):
		return self.name

class BrewPub(models.Model):
	name=models.CharField(max_length=20)
	onTap = models.CharField(max_length=100)
	bio = models.CharField(max_length=500)
	region = models.CharField(max_length=20)

	class Meta:
		ordering = ['name']
	def __unicode__(self):
		return self.name

class BrewPubBeer(models.Model):
	name=models.CharField(max_length=20)
	brewpub=models.ForeignKey(BrewPub)
	bio = models.CharField(max_length=500)

	class Meta:
		ordering = ['name']
		verbose_name="BrewPub Beer"
		verbose_name_plural = "BrewPub Beers"
	def __unicode__(self):
		return self.name

class Bar(models.Model):
	name = models.CharField(max_length=20)
	about = models.CharField(max_length=500)
	region = models.CharField(max_length=20)

	class Meta:
		ordering = ['name']
	def __unicode__(self):
		return str(self.name)

class Beer(models.Model):
	name=models.CharField(max_length=20)
	style = models.CharField(max_length=20)
	brewery=models.ForeignKey(Brewery)
	bar = models.ManyToManyField(Bar, blank=True)
	bio = models.CharField(max_length=500)

	class Meta:
		ordering = ['name']
	def __unicode__(self):
		return self.name

class Announcement(models.Model):
	name=models.CharField(max_length=15)
	content=models.CharField(max_length=50)
	url=models.CharField(max_length=20)
	pub_date= models.DateField()
	#region = models.CharField(max_length = 20)
	
	class Meta:
		get_latest_by = "pub_date"
		ordering = ['pub_date']
	def __unicode__(self):
		return self.name

class Contact(models.Model):
	subject = models.CharField(max_length=100)
	body = models.CharField(max_length=200)
	sender = models.EmailField()

##ContentTypes

class Image(models.Model):
	BAR='Bar'
	BEER ='Beer'
	BREWPUB ='BrewPub'
	BREWPUBBEER ='BrewPub Beer'
	BREWERY ='Brewery'
	ANNOUNCEMENT ='Announcement'
	OBJECT_CHOICES = (
		(BAR, tuple(Bar.objects.values_list('id','name')),),
		(BEER, tuple(Beer.objects.values_list('id','name')),),
		(BREWPUB, tuple(BrewPub.objects.values_list('id','name')),),
		(BREWPUBBEER, tuple(BrewPubBeer.objects.values_list('id','name')),),
		(BREWERY, tuple(Brewery.objects.values_list('id','name')),),
		(ANNOUNCEMENT, tuple(Announcement.objects.values_list('id','name')),),)

#Would preferably have 1 selection that gets both object id's and model name
#to supply content_type and object ID.. 

	obj = models.CharField(max_length= 20, choices=OBJECT_CHOICES)
	name = models.CharField(max_length=20)
	image = models.ImageField(upload_to="images")
	content_type= models.ForeignKey(ContentType)
	object_id = obj
	content_object = generic.GenericForeignKey('content_type', 'object_id')

	def __unicode__(self):
		return self.name

class Video(models.Model):
	BAR='Bar'
	BEER ='Beer'
	BREWPUB ='BrewPub'
	BREWPUBBEER ='BrewPub Beer'
	BREWERY ='Brewery'
	ANNOUNCEMENT =' Announcement'
	TYPE_OF_SUBJECT_CHOICES = (
		(BAR, (
			('test','test'),
			('test1', 'test1'),
			)
		),
		(BEER, (
			('test','test'),
			('test1', 'test1'),
			)
		),
		(BREWPUB, 'BrewPub'),
		(BREWPUBBEER, 'BrewPub Beer'),
		(BREWERY, 'Brewery'),
		(ANNOUNCEMENT, ' Announcement'),)
	name = models.CharField(max_length=20)
	video = models.FileField(upload_to='video/')
	subject=models.CharField(max_length=15,choices = TYPE_OF_SUBJECT_CHOICES)
	content_type=models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object=generic.GenericForeignKey('content_type', 'object_id')

	def __unicode__(self):
		return self.name