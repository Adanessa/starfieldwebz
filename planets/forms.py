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
        unique_resources = get_unique_resources()
        mapped_resources = [(map_chemical_symbols(resource), map_display_names(map_chemical_symbols(resource))) for resource in unique_resources]
        
        self.fields['resources'] = forms.MultipleChoiceField(
            choices=mapped_resources,
            widget=forms.CheckboxSelectMultiple,
            required=False
        )


