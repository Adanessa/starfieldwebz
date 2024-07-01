from django import forms
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from .models import Systems, Planets, ManufacturedItem
from .utils import get_unique_resources, map_chemical_symbols

class TagWidget(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = []
        output = []
        for val in value:
            output.append('<span style="border: 1px solid #ccc; padding: 2px 6px; margin-right: 5px;">{0} <a href="#" style="color: red; text-decoration: none;">x</a></span>'.format(conditional_escape(val)))
        output.append(super().render(name, None, attrs))  # Call the parent class's render method correctly
        return mark_safe(''.join(output))

    def value_from_datadict(self, data, files, name):
        return data.getlist(name)

    def format_value(self, value):
        if isinstance(value, (list, tuple)):
            return ', '.join(str(v) for v in value)
        return value

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
    multiple_systems = forms.BooleanField(required=False, initial=False)
    excluded_systems = forms.CharField(label='Excluded Systems', required=False, widget=TagWidget(attrs={'placeholder': 'Enter excluded systems'}))
    manufactured_items = forms.ModelMultipleChoiceField(
        queryset=ManufacturedItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Manufactured Items"
    )
    show_all_resources = forms.BooleanField(required=False, initial=False)

