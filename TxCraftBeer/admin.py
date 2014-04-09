from django.contrib import admin
from django.forms.fields import ChoiceField
from forms import Image
from TxCraftBeer.models import Beer, Brewery, Bar, BrewPub, BrewPubBeer, Announcement, Image, Video

class ImageForm(admin.ModelAdmin):
	BAR='Bar'
	BEER ='Beer'
	BREWPUB ='BrewPub'
	BREWPUBBEER ='BrewPub Beer'
	BREWERY ='Brewery'
	ANNOUNCEMENT =' Announcement'
	OBJECT_CHOICES = (
		(BAR, [Bar.objects.values_list('id','name'), 'Bar']),
		(BEER, [Beer.objects.values_list('id','name'), 'Beer']),
		(BREWPUB, [BrewPub.objects.values_list('id','name'),'BrewPub']),
		(BREWPUBBEER, [BrewPubBeer.objects.values_list('id','name'),'BrewPubBeer']),
		(BREWERY, [Brewery.objects.values_list('id','name'),'Brewery']),
		(ANNOUNCEMENT, [Announcement.objects.values_list('id','name'),'Announcement']),)
	fields=('obj',)
	exclude = ['object_id', 'content_type',]
	obj = ChoiceField(choices = OBJECT_CHOICES)
	form = Image


admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Bar)
admin.site.register(BrewPub)
admin.site.register(Announcement)
admin.site.register(Image)
admin.site.register(Video)