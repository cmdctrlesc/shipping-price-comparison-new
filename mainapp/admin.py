from django.contrib import admin
from mainapp.models import Country, Price, Surcharge

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'zone', 'provider', 'service')
    list_filter = ('provider', 'zone', 'service' )

class PriceAdmin(admin.ModelAdmin):
    list_display = ('zone', 'amount', 'weight_category', 'provider', 'service')
    list_filter = ('zone', 'provider', 'service')

admin.site.register(Country, CountryAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Surcharge)
