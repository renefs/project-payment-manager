__author__ = 'rene'
from django import forms

class ProfileEditForm(forms.Form):
    first_name=forms.CharField(required=True,max_length=100)
    last_name=forms.CharField(required=True,max_length=100)
    website=forms.URLField(required=True);
    email=forms.EmailField(required=True, label='Your e-mail address')

    #Facturacion
    billing_first_name=forms.CharField(required=True,max_length=100)
    billing_last_name=forms.CharField(required=True,max_length=100)
    billing_cif=forms.CharField(required=True,max_length=30)
    billing_city=forms.CharField(required=True,max_length=100)
    billing_province=forms.CharField(required=True,max_length=100)
    billing_country=forms.CharField(required=True,max_length=100)