from django import forms
from django.contrib import admin
from django.forms.fields import ChoiceField
from .models import Brewery,BrewPub, BrewPubBeer, Beer,Bar, Announcement, Contact, Image, Video

class Brewery(forms.ModelForm):
	class meta:
		model = Brewery

class BrewPub(forms.ModelForm):
	class meta:
		model = BrewPub

class Beer(forms.ModelForm):
	class meta:
		model = Beer

class Bar(forms.ModelForm):
	class meta:
		model = Bar

class Announcement(forms.ModelForm):
	class meta:
		model = Announcement

class Contact(forms.Form):
	class meta:
		model = Contact

class Image(forms.ModelForm):
	class Meta:
		model = Image