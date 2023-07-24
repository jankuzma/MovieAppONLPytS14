from django import forms
from django.core.exceptions import ValidationError


def is_capitalized(value):
    if not value[0].isupper():
        raise ValidationError('musi sie zaczynać wielką literą')

def max_value(value):
    if value < 1920:
        raise ValidationError('nie było żadnych producentów filmowych przed 1920')

class AddPersonForm(forms.Form):
    first_name = forms.CharField(max_length=5)
    last_name = forms.CharField(max_length=123)
    year = forms.IntegerField()

class AddProducderForm(forms.Form):
    name = forms.CharField(max_length=5, validators=[is_capitalized])
    city = forms.CharField(max_length=123, validators=[is_capitalized])
    year = forms.IntegerField(validators=[max_value])