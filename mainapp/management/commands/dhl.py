import xlrd
from mainapp.models import Price, Country
from .utils import generate_weight_categories, generate_prices


#generate prices objects for DHL
def upload_prices_dhl():
    weight_categories = generate_weight_categories()
    zones_express = [x for x in range(1, 10)]
    zones_econonmy = [x for x in range(1, 5)]
    prices_express = generate_prices(categories=weight_categories, zones=zones_express, provider='DHL', service='DHL express worldwide')
    prices_economy = generate_prices(categories=weight_categories, zones=zones_econonmy, provider='DHL', service='DHL economy select')
    prices = prices_express + prices_economy
    price_objects = Price.objects.bulk_create(prices)


def upload_countries_dhl_express():
    wb = xlrd.open_workbook('mainapp/management/commands/DHL cenik 2021 SI_SID00I6U7_slv_20201221-083938-869.xls')
    sheet = wb.sheet_by_index(2)
    objs = []
    for x in range(4, 63):
        objs.append(Country(name=sheet.cell_value(x, 0), code=sheet.cell_value(x, 0), zone=sheet.cell_value(x, 1), provider='DHL' , service='DHL express worldwide'))

    for x in range(4, 62):
        objs.append(Country(name=sheet.cell_value(x, 3), code=sheet.cell_value(x, 3), zone=sheet.cell_value(x, 4), provider='DHL' , service='DHL express worldwide'))
        objs.append(Country(name=sheet.cell_value(x, 6), code=sheet.cell_value(x, 6), zone=sheet.cell_value(x, 7), provider='DHL' , service='DHL express worldwide'))   
        objs.append(Country(name=sheet.cell_value(x, 9), code=sheet.cell_value(x, 9), zone=sheet.cell_value(x, 10), provider='DHL' , service='DHL express worldwide'))     

    countries = Country.objects.bulk_create(objs)


def upload_countries_dhl_economy():
    wb = xlrd.open_workbook('mainapp/management/commands/DHL cenik 2021 SI_SID00I6U7_slv_20201221-083938-869.xls')
    sheet = wb.sheet_by_index(5)
    objs = []
    for x in range(4, 11):
        objs.append(Country(name=sheet.cell_value(x, 0), code=sheet.cell_value(x, 0), zone=sheet.cell_value(x, 1), provider='DHL' , service='DHL economy select'))
        objs.append(Country(name=sheet.cell_value(x, 3), code=sheet.cell_value(x, 3), zone=sheet.cell_value(x, 4), provider='DHL' , service='DHL economy select'))
        objs.append(Country(name=sheet.cell_value(x, 6), code=sheet.cell_value(x, 6), zone=sheet.cell_value(x, 7), provider='DHL' , service='DHL economy select')) 

    for x in range(4, 10):    
        objs.append(Country(name=sheet.cell_value(x, 9), code=sheet.cell_value(x, 9), zone=sheet.cell_value(x, 10), provider='DHL' , service='DHL economy select')) 

    countries = Country.objects.bulk_create(objs)     


