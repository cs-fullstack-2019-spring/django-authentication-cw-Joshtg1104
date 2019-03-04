from django import forms
from .models import calorieModel


class calorieForm(forms.ModelForm):
    class Meta:
        model = calorieModel
        exclude = ["CalUserForeignKey"]
