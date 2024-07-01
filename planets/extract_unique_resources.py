from collections import defaultdict
from planets.models import Planets, CraftingMaterial

def get_unique_resource_names():
    unique_resources = defaultdict(set)

    # Gather resources from planets
    planet_resources = Planets.objects.values_list('resources', flat=True)
    for resources in planet_resources:
        if resources:
            for resource in resources.split(', '):
                unique_resources[resource].add('Planet')

    # Gather resources from crafting materials
    crafting_materials = CraftingMaterial.objects.values_list('resource_name', flat=True)
    for resource in crafting_materials:
        if resource:
            unique_resources[resource].add('Crafting Material')

    return unique_resources

unique_resources = get_unique_resource_names()
for resource, sources in unique_resources.items():
    print(f"{resource}: {sources}")
