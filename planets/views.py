# views.py

from django.shortcuts import render
from .forms import PlanetSearchForm
from .models import Planets, Systems, ManufacturedItem
from collections import defaultdict

def search_planets(request):
    form = PlanetSearchForm()
    return render(request, 'planets/search_form.html', {'form': form})

def gather_materials(item_names):
    materials_needed = {}
    processed_items = set()

    def find_item(item_name):
        try:
            return ManufacturedItem.objects.get(item_name__iexact=item_name)
        except ManufacturedItem.DoesNotExist:
            return None

    def inner_gather_materials(item_name, multiplier):
        item = find_item(item_name)
        if not item:
            return

        for material in item.crafting_materials.all():
            resource_name = material.resource_name
            quantity = material.quantity * multiplier

            materials_needed[resource_name] = materials_needed.get(resource_name, 0) + quantity

            if resource_name not in processed_items:
                processed_items.add(resource_name)
                inner_gather_materials(resource_name, quantity)

    for item_name in item_names:
        inner_gather_materials(item_name, 1)

    return materials_needed

def search_results(request):
    form = PlanetSearchForm(request.POST or None)
    planets_info = None

    if form.is_valid():
        main_planet = form.cleaned_data['main_planet']
        resources = form.cleaned_data['resources']
        include_domesticables = form.cleaned_data['include_domesticables']
        include_gatherable = form.cleaned_data['include_gatherable']
        habitability_rank = form.cleaned_data['habitability_rank']
        multiple_systems = form.cleaned_data['multiple_systems']
        excluded_systems = form.cleaned_data['excluded_systems']
        show_all_resources = form.cleaned_data.get('show_all_resources', False)  # Handle missing field
        manufactured_items = form.cleaned_data['manufactured_items']

        # Gather materials from manufactured items
        item_names = [item.item_name for item in manufactured_items]
        materials_from_items = gather_materials(item_names)
        
        # Combine these materials with the user's selected resources
        combined_resources = set(resources) | set(materials_from_items.keys())

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
                if resource in combined_resources:
                    resource_to_planets[resource].append(planet)
        
        # Use a greedy algorithm to cover all resources with the minimum number of planets
        selected_planets = set()
        covered_resources = set()
        while covered_resources != combined_resources:
            best_planet = None
            best_covered = set()
            for planet in planets:
                if planet in selected_planets:
                    continue
                planet_resources = set(planet.resources.split(', '))
                newly_covered = planet_resources & combined_resources - covered_resources
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
            matching_resources = planet_resources & combined_resources
            all_resources = planet_resources if show_all_resources else matching_resources
            detailed_planet_info.append({
                'planet': planet,
                'matching_resources': matching_resources,
                'all_resources': all_resources
            })

        planets_info = detailed_planet_info

    context = {
        'form': form,
        'planets_info': planets_info
    }

    return render(request, 'planets/search_results.html', context)
