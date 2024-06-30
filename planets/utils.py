from .models import Planets

def get_unique_resources():
    all_resources = Planets.objects.values_list('resources', flat=True)
    resource_set = set()
    for resource_list in all_resources:
        if resource_list:
            resources = resource_list.split(',')
            for resource in resources:
                resource_set.add(resource.strip())
    return sorted(resource_set)

CHEMICAL_SYMBOLS = {
    'Al': 'Aluminium',
    'Cl': 'Chlorine',
    'H2O': 'Water',
    'He-3': 'Helium-3',
    'Li': 'Lithium',
    'Cu': 'Copper',
    'Pb': 'Lead',
    'Ni': 'Nickel',
    'Co': 'Cobalt',
    'F': 'Fluorine',
    'Ag': 'Silver',
    'Hg': 'Mercury',
    'Ct': 'Carbon',

}

def map_chemical_symbols(resources):
    mapped_resources = []
    for resource in resources:
        full_name = CHEMICAL_SYMBOLS.get(resource, resource)
        mapped_resources.append((resource, full_name))
    return mapped_resources
