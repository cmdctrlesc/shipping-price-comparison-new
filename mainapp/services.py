from .models import Price, Surcharge, Country
from django.db.models import Q

def generate_weight_categories():
    categories = []
    for x in range (0, 100):
        if x % 5 == 0:
            categories.append((x, x+5))

    return categories


def get_weight_category(num):

    categories = generate_weight_categories()

    for category in categories:
        if category[0] < num < category[1]:
            return category[1]


def get_price_from_input(country_code_input, weight_input, provider, service):
    country = Country.objects.filter(Q(code=country_code_input) | Q(code__contains=country_code_input), provider=provider, service=service ).first()
    zone = country.zone
    weight_category = get_weight_category(weight_input)
    price = Price.objects.get(zone=zone, weight_category=weight_category , provider=provider, service=service)
    surcharges = Surcharge.objects.filter(provider=provider, service=service)

    if surcharges:
        surcharges = sum([surcharge.amount for surcharge in surcharges])
        final_price = price.amount + surcharges

        return final_price

    else:
        return price.amount
