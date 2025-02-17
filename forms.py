from django import forms
from test_app.models import*

class Contactform(forms.ModelForm):
    class Meta:
        model= contactenquiry
        fields=('name','email','massege')


    # name=forms.CharField(max_length=100)
    # email=forms.EmailField()
    # message=forms.CharField(max_length=100)