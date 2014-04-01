from django.contrib import admin
from TxCraftBeer.models import Beer, Brewery, Bar, BrewPub, Announcement

#class BeerAdmin(admin.ModelAdmin):
#	list_display=('name','address','bio')

admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Bar)
admin.site.register(BrewPub)
admin.site.register(Announcement)