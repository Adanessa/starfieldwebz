from django.shortcuts import render
from .utils import map_chemical_symbols, map_display_names
from .forms import PlanetSearchForm
from .models import Planets, Systems, ManufacturedItem
from collections import defaultdict

def show_system_resources(selected_systems):
    system_resources = {}
    for system in selected_systems:
        try:
            system_instance = Systems.objects.get(name=system)
            resources = system_instance.system_resources.split(', ') if system_instance.system_resources else []
            system_resources[system_instance.name] = resources
        except Systems.DoesNotExist:
            continue
    return system_resources
    

def gather_materials(item_names):
    materials_needed = {}
    for item_name in item_names:
        try:
            manufactured_item = ManufacturedItem.objects.get(item_name__iexact=item_name)
            for material in manufactured_item.crafting_materials.all():
                resource_name = map_chemical_symbols(material.resource_name)
                materials_needed[resource_name] = True  # Use a dummy value
        except ManufacturedItem.DoesNotExist:
            continue
    return materials_needed

def filter_planets_by_habitability(planets, habitability_rank):
    if habitability_rank is not None:
        return [planet for planet in planets if planet.hab_rank and planet.hab_rank.isdigit() and int(planet.hab_rank) <= habitability_rank]
    return planets

def map_resources_to_planets(planets, combined_resources):
    resource_to_planets = defaultdict(list)
    for planet in planets:
        planet_resources = planet.resources.split(', ')
        for resource in planet_resources:
            mapped_resource = map_chemical_symbols(resource)
            if mapped_resource in combined_resources:
                resource_to_planets[mapped_resource].append(planet)
    return resource_to_planets

def select_best_planets(planets, combined_resources):
    selected_planets = set()
    covered_resources = set()
    while covered_resources != combined_resources:
        best_planet = None
        best_covered = set()
        for planet in planets:
            if planet in selected_planets:
                continue
            planet_resources = set(map_chemical_symbols(r) for r in planet.resources.split(', '))
            newly_covered = planet_resources & combined_resources - covered_resources
            if len(newly_covered) > len(best_covered):
                best_planet = planet
                best_covered = newly_covered
        if not best_planet:
            break
        selected_planets.add(best_planet)
        covered_resources.update(best_covered)
        print(f"Selected planets: {selected_planets}, Covered resources: {covered_resources}")
    return selected_planets, covered_resources

def select_system_planets(planets, combined_resources):
    for system in Systems.objects.all():
        system_planets = planets.filter(system=system)
        system_resources = set()
        system_planet_set = set()
        for planet in system_planets:
            planet_resources = set(map_chemical_symbols(r) for r in planet.resources.split(', '))
            system_resources.update(planet_resources)
            system_planet_set.add(planet)
            if combined_resources.issubset(system_resources):
                return system_planet_set, combined_resources
    return set(), set()

def prepare_planet_info(selected_planets, combined_resources, show_all_resources):
    detailed_planet_info = []
    for planet in selected_planets:
        planet_resources = set(map_chemical_symbols(r) for r in planet.resources.split(', '))
        matching_resources = planet_resources & combined_resources
        all_resources = planet_resources if show_all_resources else matching_resources
        detailed_planet_info.append({
            'planet': planet,
            'matching_resources': {map_display_names(res) for res in matching_resources},
            'all_resources': {map_display_names(res) for res in all_resources},
            'hab_rank': planet.hab_rank
        })
    return detailed_planet_info

def search_results(request):
    form = PlanetSearchForm(request.POST or None)
    planets_info = None
    system_resources = None

    if form.is_valid():
        print("Form is valid")
        cleaned_data = form.cleaned_data
        inorganic_resources = cleaned_data['inorganic_resources']
        organic_resources = cleaned_data['organic_resources']
        habitability_rank = cleaned_data['habitability_rank']
        multiple_systems = cleaned_data['multiple_systems']
        show_all_resources = cleaned_data.get('show_all_resources', False)
        manufactured_items = cleaned_data['manufactured_items']
        selected_systems = cleaned_data.get('selected_systems', [])
        system_resources = show_system_resources(selected_systems)

        item_names = [item.item_name for item in manufactured_items]
        materials_from_items = gather_materials(item_names)
        combined_resources = set(inorganic_resources) | set(organic_resources) | set(materials_from_items.keys())

        print(f"Combined resources: {combined_resources}")

        planets = Planets.objects.all()
        print(f"Initial planets count: {planets.count()}")

        planets = filter_planets_by_habitability(planets, habitability_rank)

        resource_to_planets = map_resources_to_planets(planets, combined_resources)
        print(f"Resource to planets mapping: {dict(resource_to_planets)}")

        if multiple_systems:
            selected_planets, covered_resources = select_best_planets(planets, combined_resources)
        else:
            selected_planets, covered_resources = select_system_planets(planets, combined_resources)

        planets_info = prepare_planet_info(selected_planets, combined_resources, show_all_resources)

    else:
        print("Form is not valid")

    context = {
        'form': form,
        'planets_info': planets_info,
        'system_resources': system_resources,
    }

    return render(request, 'planets/search_results.html', context)
