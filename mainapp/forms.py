from django import forms

class MyForm(forms.Form):
    country_code = forms.CharField(max_length=100, label="Country code (ISO Alpha-2)")
    weight = forms.CharField(max_length=100, label="Weight (float or int, must not be 0)")