from django.shortcuts import render
from .utils import map_chemical_symbols, map_display_names
from .forms import PlanetSearchForm
from .models import Planets, Systems, ManufacturedItem
from collections import defaultdict

# Function to gather materials needed for manufactured items
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

# View function to handle search results based on form inputs
def search_results(request):
    form = PlanetSearchForm(request.POST or None)
    planets_info = None
    incomplete_search = False

    if form.is_valid():
        main_planet = form.cleaned_data['main_planet']
        inorganic_resources = form.cleaned_data['inorganic_resources']
        organic_resources = form.cleaned_data['organic_resources']
        include_domesticables = form.cleaned_data['include_domesticables']
        include_gatherable = form.cleaned_data['include_gatherable']
        habitability_rank = form.cleaned_data['habitability_rank']
        multiple_systems = form.cleaned_data['multiple_systems']
        excluded_systems = form.cleaned_data.get('excluded_systems', [])
        show_all_resources = form.cleaned_data.get('show_all_resources', False)
        manufactured_items = form.cleaned_data['manufactured_items']

        item_names = [item.item_name for item in manufactured_items]
        materials_from_items = gather_materials(item_names)
        combined_resources = set(inorganic_resources) | set(organic_resources) | set(materials_from_items.keys())

        planets = Planets.objects.all()

        # Filter planets based on main planet selection and ensure it is in the results
        if main_planet:
            if habitability_rank is not None and (main_planet.hab_rank and main_planet.hab_rank.isdigit() and int(main_planet.hab_rank) > habitability_rank):
                main_planet = None  # If the main planet does not meet the habitability rank, set it to None
            else:
                planets = planets.filter(system=main_planet.system)

        # Include domesticables into the search if you want to see if chosen organic materials can be farmed via outpost.
        if include_domesticables:
            planets = planets.filter(domesticable__isnull=False)

        if include_gatherable:
            planets = planets.filter(gatherable__isnull=False)

        # Include to set users current habitability level to make sure no planets that have higher hab rank req are chosen
        if habitability_rank is not None:
            planets = [
                planet for planet in planets
                if planet.hab_rank and planet.hab_rank.isdigit() and int(planet.hab_rank) <= habitability_rank
            ]

        if excluded_systems:
            planets = planets.exclude(system__in=excluded_systems)

        resource_to_planets = defaultdict(list)
        for planet in planets:
            planet_resources = planet.resources.split(', ')
            for resource in planet_resources:
                mapped_resource = map_chemical_symbols(resource)
                if mapped_resource in combined_resources:
                    resource_to_planets[mapped_resource].append(planet)

        selected_planets = set()
        covered_resources = set()

        # Add main planet if it meets criteria
        if main_planet:
            main_planet_resources = set(map_chemical_symbols(r) for r in main_planet.resources.split(', '))
            selected_planets.add(main_planet)
            covered_resources.update(main_planet_resources & combined_resources)

        # Select planets to cover all combined resources
        if multiple_systems:
            while covered_resources != combined_resources:
                best_planet = None
                best_covered = set()
                for planet in Planets.objects.exclude(system__in=excluded_systems):
                    if planet in selected_planets:
                        continue
                    if habitability_rank is not None and (planet.hab_rank and planet.hab_rank.isdigit() and int(planet.hab_rank) > habitability_rank):
                        continue
                    planet_resources = set(map_chemical_symbols(r) for r in planet.resources.split(', '))
                    newly_covered = planet_resources & combined_resources - covered_resources
                    if len(newly_covered) > len(best_covered):
                        best_planet = planet
                        best_covered = newly_covered
                if not best_planet:
                    incomplete_search = True
                    break
                selected_planets.add(best_planet)
                covered_resources.update(best_covered)
        else:
            for system in Systems.objects.all():
                if system in excluded_systems:
                    continue
                system_planets = planets.filter(system=system)
                system_resources = set()
                system_planet_set = set()
                for planet in system_planets:
                    planet_resources = set(map_chemical_symbols(r) for r in planet.resources.split(', '))
                    system_resources.update(planet_resources)
                    system_planet_set.add(planet)
                    if combined_resources.issubset(system_resources):
                        selected_planets.update(system_planet_set)
                        covered_resources = combined_resources
                        break
                if covered_resources == combined_resources:
                    break
            if covered_resources != combined_resources:
                incomplete_search = True

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

        planets_info = detailed_planet_info

    context = {
        'form': form,
        'planets_info': planets_info,
        'incomplete_search': incomplete_search,
    }

    return render(request, 'planets/search_results.html', context)
