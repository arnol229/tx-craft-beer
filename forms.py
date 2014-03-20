from django import forms
from .models import Brewery,BrewPub,Beer,Bar, Announcements

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

class Announcements(forms.ModelForm):
	class meta:
		model = Announcements