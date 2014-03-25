from django.contrib import admin
from models import Beer, Brewery, Bar, BrewPub

class BeerAdmin(admin.ModelAdmin):
	list_display=('name','address','bio')

admin.site.register(Beer, BeerAdmin)
admin.site.register(Brewery)
admin.site.register(Bar)
admin.site.register(BrewPub)