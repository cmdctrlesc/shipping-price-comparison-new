from mainapp.services import get_weight_category
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .models import Country, Price, Surcharge
from .services import get_price_from_input

def main_view(request):

    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            try:
                country_code_input= form.cleaned_data['country_code']
                weight_input = float(form.cleaned_data['weight'])
                dhl_express = get_price_from_input(country_code_input=country_code_input, weight_input=weight_input, provider='DHL', service='DHL express worldwide')
                dhl_economy = get_price_from_input(country_code_input=country_code_input, weight_input=weight_input, provider='DHL', service='DHL economy select')
                ups_express = get_price_from_input(country_code_input=country_code_input, weight_input=weight_input, provider='UPS', service='UPS express saver')
                ups_standard = get_price_from_input(country_code_input=country_code_input, weight_input=weight_input, provider='UPS', service='UPS standard')
                tnt_express = get_price_from_input(country_code_input=country_code_input, weight_input=weight_input, provider='TNT', service='TNT express')
                tnt_economy = get_price_from_input(country_code_input=country_code_input, weight_input=weight_input, provider='TNT', service='TNT economy')

                results_dict = {"dhl_express": dhl_express,
                                "dhl_economy":dhl_economy, 
                                "ups_express": ups_express,
                                "ups_standard": ups_standard,
                                "tnt_express": tnt_express,
                                "tnt_economy": tnt_economy}

                return render(request, "yourresult.html", results_dict)
            except:

                return render(request, "fail.html")
    else:
        form = MyForm()
    return render(request, "main.html", {"form": form})