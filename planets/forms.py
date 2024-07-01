from django import forms
from .models import Systems, Planets, ManufacturedItem
from .utils import get_unique_resources, map_chemical_symbols


class ResourceForm(forms.Form):
    resources = forms.CharField(label='Resources (comma-separated)', max_length=255)
    include_biomes = forms.BooleanField(required=False, label="Include Biomes")
    include_type = forms.BooleanField(required=False, label="Include Type")
    
    
class PlanetSearchForm(forms.Form):
    main_planet = forms.ModelChoiceField(queryset=Planets.objects.all(), required=False)
    
    unique_resources = get_unique_resources()
    resource_choices = map_chemical_symbols(unique_resources)
    
    resources = forms.MultipleChoiceField(
        choices=resource_choices,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    include_domesticables = forms.BooleanField(required=False, initial=False)
    include_gatherable = forms.BooleanField(required=False, initial=False)
    habitability_rank = forms.IntegerField(min_value=0, max_value=4, required=False)
    multiple_systems = forms.BooleanField(required=False, initial=True)
    excluded_systems = forms.ModelMultipleChoiceField(queryset=Systems.objects.all(), required=False)
    manufactured_items = forms.ModelMultipleChoiceField(
        queryset=ManufacturedItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Manufactured Items"
    )
    show_all_resources = forms.BooleanField(required=False, initial=False)

