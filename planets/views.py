from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import ResourceForm
from .models import Planets, Systems


def resource_search(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resources_input = form.cleaned_data['resources']
            resources_list = [resource.strip() for resource in resources_input.split(',')]
            include_biomes = form.cleaned_data['include_biomes']
            include_type = form.cleaned_data['include_type']
            
            # Add more fields (Delete these when you understand how to add 1 + 1)
            fields_to_include = {
                'type': include_type,
                'biomes': include_biomes
            }
            
            # Filter planets that contain all specified resources
            planets = Planets.objects.select_related('system').all() 
            for resource in resources_list:
                planets = planets.filter(resources__icontains=resource)
            
            context = {
                'form': form,
                'planets': planets,
                'fields_to_include': fields_to_include,
            }
            return render(request, 'planets/resource_search_results.html', context)
    else:
        form = ResourceForm()

    return render(request, 'planets/resource_search.html', {'form': form})



def planet_table(request):
    planets_list = Planets.objects.all()  # Fetch all planets from the database
    paginator = Paginator(planets_list, 50)
    
    page_number = request.GET.get('page')
    planets = paginator.get_page(page_number)
    return render(request, 'planets/planet_table.html', {'planets': planets})
