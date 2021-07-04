import xlrd
from mainapp.models import Price, Country
from .utils import generate_weight_categories, generate_prices

def upload_prices_tnt():
    weight_categories = generate_weight_categories()
    zones = [x for x in range(1, 10)]
    prices_express = generate_prices(categories=weight_categories, zones=zones, provider='TNT', service='TNT express')
    prices_economy = generate_prices(categories=weight_categories, zones=zones, provider='TNT', service='TNT economy')
    prices = prices_express + prices_economy
    price_objects = Price.objects.bulk_create(prices)

def upload_countries_tnt():
    wb = xlrd.open_workbook('mainapp/management/commands/tnt mednarodni cenik 2021 - 1si09.xls')
    sheet = wb.sheet_by_index(2)
    objs = []
    for x in range(7, 53):
        objs.append(Country(name=sheet.cell_value(x, 0), code=sheet.cell_value(x, 2), zone=sheet.cell_value(x, 4), provider='TNT' , service='TNT express'))
        objs.append(Country(name=sheet.cell_value(x, 0), code=sheet.cell_value(x, 2), zone=sheet.cell_value(x, 4), provider='TNT' , service='TNT economy'))

    for x in range(7, 56):
        objs.append(Country(name=sheet.cell_value(x, 6), code=sheet.cell_value(x, 8), zone=sheet.cell_value(x, 10), provider='TNT' , service='TNT express'))
        objs.append(Country(name=sheet.cell_value(x, 6), code=sheet.cell_value(x, 8), zone=sheet.cell_value(x, 10), provider='TNT' , service='TNT economy'))
        objs.append(Country(name=sheet.cell_value(x, 12), code=sheet.cell_value(x, 14), zone=sheet.cell_value(x, 16), provider='TNT' , service='TNT express'))
        objs.append(Country(name=sheet.cell_value(x, 12), code=sheet.cell_value(x, 14), zone=sheet.cell_value(x, 16), provider='TNT' , service='TNT economy'))
  

    countries = Country.objects.bulk_create(objs)   

