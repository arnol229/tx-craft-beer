from django.db import models
import os
import datetime

class Brewery(models.Model):
	name=models.CharField(max_length=20)
	address=models.CharField(max_length=50)
	bio = models.CharField(max_length=500)
	pic = models.ImageField(upload_to="images/Brewery/")
	region = models.CharField(max_length=20)
	video = models.FileField(upload_to="video/Brewery/")

	class Meta:
		ordering = ['name']
		verbose_name_plural = "Breweries"
	def __unicode__(self):
		return self.name

class BrewPub(models.Model):
	name=models.CharField(max_length=20)
	bio = models.CharField(max_length=500)
	pic = models.ImageField(upload_to="images/BrewPub/")
	region = models.CharField(max_length=20)
	video = models.FileField(upload_to="video/BrewPub/")

	class Meta:
		ordering = ['name']
	def __unicode__(self):
		return self.name

class Beer(models.Model):
	name=models.CharField(max_length=20)
	brewery=models.ForeignKey(Brewery)
	bio = models.CharField(max_length=500)
	pic = models.ImageField(upload_to="images/Beer/")

	class Meta:
		ordering = ['name']
	def __unicode__(self):
		return self.name

class BrewPubBeer(models.Model):
	name=models.CharField(max_length=20)
	brewpub=models.ForeignKey(BrewPub)
	bio = models.CharField(max_length=500)
	pic = models.ImageField(upload_to="images/BrewPubBeer/")

	class Meta:
		ordering = ['name']
		verbose_name="BrewPub Beer"
		verbose_name_plural = "BrewPub Beers"
	def __unicode__(self):
		return self.name

class Bar(models.Model):
	name = models.CharField(max_length=20)
	bio=models.CharField(max_length=500)
	pic=models.ImageField(upload_to="images/Bar/")
	region = models.CharField(max_length=20)
	video = models.FileField(upload_to="video/Bar")

	class Meta:
		ordering = ['name']
	def __unicode__(self):
		return self.name

class Announcement(models.Model):
	name=models.CharField(max_length=15)
	content=models.CharField(max_length=50)
	pic=models.ImageField(upload_to="images/Announcments/")
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

