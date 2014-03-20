from django.db import models
import os

class Brewery(models.Model):
	name=models.CharField(max_length=20)
	address=models.CharField(max_length=50)

class BrewPub(models.Model):
	name=models.CharField(max_length=20)

class Beer(models.Model):
	name=models.CharField(max_length=20)
	brewery=models.ForeignKey(Brewery)

class BrewPubBeer(models.Model):
	name=models.CharField(max_length=20)
	brewpub=models.ForeignKey(BrewPub)

class Announcments(models.Model):
	title=models.CharField(max_length=15)
	content=models.CharField(max_length=50)

