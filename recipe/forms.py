from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "ingredients", "steps", "image", "category"]

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Search")
