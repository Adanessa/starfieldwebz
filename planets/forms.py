from django import forms
from .models import Planets, Systems, ManufacturedItem
from .utils import get_unique_resources, map_chemical_symbols, map_display_names

class PlanetSearchForm(forms.Form):
    main_planet = forms.ModelChoiceField(queryset=Planets.objects.all(), required=False)
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Dynamically retrieve and map resource choices
        resource_choices = get_unique_resources()

        # Seperate inorganic from organic.
        self.fields['inorganic_resources'] = forms.MultipleChoiceField(
            choices=[(r, map_display_names(r)) for r in resource_choices['inorganic_resources']],
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label="Inorganic Resources"
        )
        # Seperate organics from inorganic.
        self.fields['organic_resources'] = forms.MultipleChoiceField(
            choices=[(r, map_display_names(r)) for r in resource_choices['organic_resources']],
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label="Organic Resources"
        )