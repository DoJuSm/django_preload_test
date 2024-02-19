from django import forms
from .models import MomCat, Kitten

class MomCatForm(forms.ModelForm):
    class Meta:
        model = MomCat
        fields = ['name', 'age', 'owners_name']

class KittenForm(forms.ModelForm):
    class Meta:
        model = Kitten
        fields = ['name', 'age_in_months']