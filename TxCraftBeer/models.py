from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
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
		return self.name

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
	name = models.CharField(max_length=20)
	image = models.ImageField(upload_to="images")
	content_type= models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')

	def __unicode__(self):
		return self.name

class Video(models.Model):
	name = models.CharField(max_length=20)
	video = models.FileField(upload_to='video/')
	content_type=models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object=generic.GenericForeignKey('content_type', 'object_id')

	def __unicode__(self):
		return self.name