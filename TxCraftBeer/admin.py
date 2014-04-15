from django.contrib import admin
from django import forms
from django.forms.fields import ChoiceField
from forms import ImageForm
from django.db import models
from TxCraftBeer.models import Beer, Brewery, Bar, BrewPub, BrewPubBeer, Announcement, Image, Video

class ImageAdmin(admin.ModelAdmin):
	fields=('name','object_id','content_type','image')
	#list_display = ('')
	form = ImageForm

admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Bar)
admin.site.register(BrewPub)
admin.site.register(Announcement)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video)