import xlrd
from mainapp.models import Price, Country
from .utils import generate_weight_categories, generate_prices


def upload_prices_ups():
    weight_categories = generate_weight_categories()
    zones_saver = [x for x in range(1, 11)]
    extra_zones_saver = [99, 702]
    all_zones_saver = zones_saver + extra_zones_saver
    prices_express = generate_prices(categories=weight_categories, zones=all_zones_saver, provider='UPS', service='UPS express saver')
    zones_standard = [x for x in range(1, 6)]
    extra_zones_standard = [703]
    all_zones_standard = zones_standard + extra_zones_standard
    prices_standard = generate_prices(categories=weight_categories, zones=all_zones_standard, provider='UPS', service='UPS standard')
    prices = prices_express + prices_standard
    price_objects = Price.objects.bulk_create(prices)      

def upload_countries_ups():
    wb = xlrd.open_workbook('mainapp/management/commands/UPS Rates Matrix Music d.o.o. 2021.xls')
    sheet = wb.sheet_by_index(4)
    objs = []
    for x in range(13, 262):
        objs.append(Country(name=sheet.cell_value(x, 3), code=sheet.cell_value(x, 1), zone=sheet.cell_value(x, 11), provider='UPS' , service='UPS express saver')) 
        if not sheet.cell_value(x, 13):
            continue
        else: 
            objs.append(Country(name=sheet.cell_value(x, 3), code=sheet.cell_value(x, 1), zone=sheet.cell_value(x, 13), provider='UPS' , service='UPS standard'))

    countries = Country.objects.bulk_create(objs)

        