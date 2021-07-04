from mainapp.models import Price

def generate_weight_categories():
    weight_categories = []
    for x in range(5, 105):
        if x % 5 == 0:
            weight_categories.append(x)
   

    return weight_categories

def generate_prices(categories, zones, provider, service):

    objs = []
    for category in categories:
        for zone in zones:
            price = Price(zone=zone, amount=0, weight_category=category, provider=provider, service=service)
            objs.append(price)

    return objs

