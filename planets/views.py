from django.shortcuts import render
from .forms import PlanetSearchForm
from .models import Planets, Systems, ManufacturedItem, CraftingMaterial
from collections import defaultdict

def gather_materials(item_names):
    materials_needed = {}
    print(f"Gathering materials for items: {item_names}")

    for item_name in item_names:
        try:
            manufactured_item = ManufacturedItem.objects.get(item_name__iexact=item_name)
            print(f"Found manufactured item: {manufactured_item}")
            for material in manufactured_item.crafting_materials.all():
                resource_name = material.resource_name
                print(f"Found crafting material: {resource_name}")
                materials_needed[resource_name] = True
        except ManufacturedItem.DoesNotExist:
            print(f"Manufactured item not found: {item_name}")
            continue

    print(f"Materials needed: {materials_needed}")
    return materials_needed


def search_results(request):
    form = PlanetSearchForm(request.POST or None)
    planets_info = None

    if form.is_valid():
        print("Form is valid")
        main_planet = form.cleaned_data['main_planet']
        resources = form.cleaned_data['resources']
        include_domesticables = form.cleaned_data['include_domesticables']
        include_gatherable = form.cleaned_data['include_gatherable']
        habitability_rank = form.cleaned_data['habitability_rank']
        multiple_systems = form.cleaned_data['multiple_systems']
        excluded_systems = form.cleaned_data.get('excluded_systems', [])
        show_all_resources = form.cleaned_data.get('show_all_resources', False)
        manufactured_items = form.cleaned_data['manufactured_items']

        item_names = [item.item_name for item in manufactured_items]
        materials_from_items = gather_materials(item_names)
        combined_resources = set(resources) | set(materials_from_items.keys())
        
        print(f"Combined resources: {combined_resources}")

        planets = Planets.objects.all()
        print(f"Initial planets count: {planets.count()}")

        # Apply filters based on form inputs
        if main_planet:
            planets = planets.filter(system=main_planet.system)
            print(f"Planets after main_planet filter: {planets.count()}")

        if include_domesticables:
            planets = planets.filter(domesticable__isnull=False)
            print(f"Planets after include_domesticables filter: {planets.count()}")

        if include_gatherable:
            planets = planets.filter(gatherable__isnull=False)
            print(f"Planets after include_gatherable filter: {planets.count()}")

        if habitability_rank is not None:
            planets = [
                planet for planet in planets
                if planet.hab_rank and planet.hab_rank.isdigit() and int(planet.hab_rank) <= habitability_rank
            ]
            print(f"Planets after habitability_rank filter: {len(planets)}")

        # Exclude systems based on names
        if excluded_systems:
            planets = planets.exclude(system__in=excluded_systems)
            print(f"Planets after excluded_systems filter: {planets.count()}")

        resource_to_planets = defaultdict(list)
        for planet in planets:
            planet_resources = planet.resources.split(', ')
            for resource in planet_resources:
                if resource in combined_resources:
                    resource_to_planets[resource].append(planet)
        print(f"Resource to planets mapping: {dict(resource_to_planets)}")

        selected_planets = set()
        covered_resources = set()

        if multiple_systems:
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
                    break
                selected_planets.add(best_planet)
                covered_resources.update(best_covered)
                print(f"Selected planets: {selected_planets}, Covered resources: {covered_resources}")
        else:
            for system in Systems.objects.all():
                system_planets = planets.filter(system=system)
                system_resources = set()
                system_planet_set = set()
                for planet in system_planets:
                    planet_resources = set(planet.resources.split(', '))
                    system_resources.update(planet_resources)
                    system_planet_set.add(planet)
                    if combined_resources.issubset(system_resources):
                        selected_planets = system_planet_set
                        covered_resources = combined_resources
                        break
                if covered_resources == combined_resources:
                    break

        detailed_planet_info = []
        for planet in selected_planets:
            planet_resources = set(planet.resources.split(', '))
            matching_resources = planet_resources & combined_resources
            all_resources = planet_resources if show_all_resources else matching_resources
            detailed_planet_info.append({
                'planet': planet,
                'matching_resources': matching_resources,
                'all_resources': all_resources,
                'hab_rank': planet.hab_rank
            })

        planets_info = detailed_planet_info

    else:
        print("Form is not valid")

    context = {
        'form': form,
        'planets_info': planets_info
    }

    return render(request, 'planets/search_results.html', context)
