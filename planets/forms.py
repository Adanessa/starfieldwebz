from django import forms

class ResourceForm(forms.Form):
    resources = forms.CharField(label='Resources (comma-separated)', max_length=255)
    include_biomes = forms.BooleanField(required=False, label="Include Biomes")
    include_type = forms.BooleanField(required=False, label="Include Type")