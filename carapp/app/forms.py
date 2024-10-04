from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['model_name', 'mfg_year', 'car_img', 'color', 'no_of_seets', 'engine_type', 'price']
