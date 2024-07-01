from django.shortcuts import render
from .models import Systems, Planets
from .forms import ResourceForm, PlanetSearchForm
from collections import defaultdict


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


def search_planets(request):
    if request.method == "POST":
        form = PlanetSearchForm(request.POST)
        if form.is_valid():
            return redirect('planets:search_results')
    else:
        form = PlanetSearchForm()
    return render(request, 'planets/search_form.html', {'form': form})

def search_results(request):
    form = PlanetSearchForm(request.POST)
    planets_info = None

    if form.is_valid():
        main_planet = form.cleaned_data['main_planet']
        resources = form.cleaned_data['resources']
        include_domesticables = form.cleaned_data['include_domesticables']
        include_gatherable = form.cleaned_data['include_gatherable']
        habitability_rank = form.cleaned_data['habitability_rank']
        multiple_systems = form.cleaned_data['multiple_systems']
        excluded_systems = form.cleaned_data['excluded_systems']

        planets = Planets.objects.all()
        if main_planet:
            planets = planets.filter(system=main_planet.system)
        
        if include_domesticables:
            planets = planets.filter(domesticable__isnull=False)
            
        if include_gatherable:
            planets = planets.filter(gatherable__isnull=False)
            
        planets = planets.filter(hab_rank__lte=habitability_rank)
        
        if excluded_systems:
            planets = planets.exclude(system__in=excluded_systems)
        
        if not multiple_systems and main_planet:
            planets = planets.filter(system=main_planet.system)

        # Create a mapping from resource to planets
        resource_to_planets = defaultdict(list)
        for planet in planets:
            planet_resources = planet.resources.split(', ')
            for resource in planet_resources:
                if resource in resources:
                    resource_to_planets[resource].append(planet)
        
        # Use a greedy algorithm to cover all resources with the minimum number of planets
        selected_planets = set()
        covered_resources = set()
        while covered_resources != set(resources):
            best_planet = None
            best_covered = set()
            for planet in planets:
                if planet in selected_planets:
                    continue
                planet_resources = set(planet.resources.split(', '))
                newly_covered = planet_resources & set(resources) - covered_resources
                if len(newly_covered) > len(best_covered):
                    best_planet = planet
                    best_covered = newly_covered
            if not best_planet:
                break  # In case we can't cover all resources
            selected_planets.add(best_planet)
            covered_resources.update(best_covered)

        # Prepare the context with detailed resource info
        detailed_planet_info = []
        for planet in selected_planets:
            planet_resources = set(planet.resources.split(', '))
            matching_resources = planet_resources & set(resources)
            detailed_planet_info.append({
                'planet': planet,
                'matching_resources': matching_resources,
                'all_resources': planet_resources
            })

        planets_info = detailed_planet_info

    context = {
        'form': form,
        'planets_info': planets_info
    }

    return render(request, 'planets/search_results.html', context)
