from django import forms
from django.contrib.auth.models import User
from myapp1.models import *

class branch_form(forms.ModelForm):
    class Meta:
        model=branch_model
        fields="__all__"
        
