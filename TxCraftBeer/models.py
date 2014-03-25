from django.db import models
import os
import datetime

class Brewery(models.Model):
	name=models.CharField(max_length=20)
	address=models.CharField(max_length=50)
	bio = models.CharField(max_length=500)
	pic = models.ImageField()

class BrewPub(models.Model):
	name=models.CharField(max_length=20)
	bio = models.CharField(max_length=500)
	pic = models.ImageField()

class Beer(models.Model):
	name=models.CharField(max_length=20)
	brewery=models.ForeignKey(Brewery)
	bio = models.CharField(max_length=500)
	pic = models.ImageField()

class BrewPubBeer(models.Model):
	name=models.CharField(max_length=20)
	brewpub=models.ForeignKey(BrewPub)
	bio = models.CharField(max_length=500)
	pic = models.ImageField()
	def __unicode__(self):
		return name

class Bar(models.Model):
	name = models.CharField(max_length=20)
	bio=models.CharField(max_length=500)
	pic=models.ImageField()

class Announcments(models.Model):
	title=models.CharField(max_length=15)
	content=models.CharField(max_length=50)
	frontPic=models.ImageField()
	url=models.CharField(max_length=20)
	pub_date= datetime.datetime.now()

	def __unicode__(self):
		return title

