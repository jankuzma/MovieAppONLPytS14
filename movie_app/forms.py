from django import forms


class AddPersonForm(forms.Form):
    first_name = forms.CharField(max_length=5)
    last_name = forms.CharField(max_length=123)
    year = forms.IntegerField()