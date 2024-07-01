from .models import Planets
RESOURCE_MAPPING = {
    'Fe': 'Fe',  # Assuming you want "Fe" to remain as "Fe"
    'Iron': 'Fe',  # Map "Iron" to "Fe"
    'Iron(Fe)': 'Fe',  # Map "Iron(Fe)" to "Fe"
    'He-3': 'He-3',  # Assuming you want "He-3" to remain as "He-3"
    'Al': 'Al',  # Map "Al" to "Al"
    'Aluminium': 'Al',  # Map "Aluminium" to "Al"
    'Aluminium(Al)': 'Al',  # Map "Aluminium(Al)" to "Al"
    'Be': 'Beryllium',
    'Beryllium': 'Beryllium',
    'Eu': 'Europium',
    'Europium': 'Europium',
    'Cl': 'Chlorine',
    'H2O': 'Water',
    'Li': 'Lithium',
    'Lithium': 'Lithium',
    'Cu': 'Copper',
    'Copper': 'Copper',
    'Cs': 'Caesium',
    'Caesium': 'Caesium',
    'Ceasium(Cs)': 'Caesium',
    'Fiber': 'Fiber',
    'Nutrient': 'Nutrient',
    'Sealant': 'Sealant',
    'Structural Material': 'Structural Material',
    'Pb': 'Lead',
    'Lead': 'Lead',
    'Ni': 'Nickel',
    'Nickel': 'Nickel',
    'Nickel(Ni)': 'Nickel',
    'U': 'Uranium',
    'Uranium': 'Uranium',
    'Pu': 'Plutonium',
    'Plutonium': 'Plutonium',
    'F': 'Fluorine',
    'Fluorine': 'Fluorine',
    'Ag': 'Silver',
    'Silver': 'Silver',
    'Hg': 'Mercury',
    'Mercury': 'Mercury',
    'Aluminium(Al)': 'Aluminium',
    'Iron(Fe)': 'Iron',
    'Aldumite(Ad)': 'Aldumite',
    'Ceasium(Cs)': 'Caesium',
    'Drilling Rig': 'Drilling Rig',
    'Microsend Regulator': 'Microsend Regulator',
    'Isocentered Magnet': 'Isocentered Magnet',
    'Tau Grade Rheostat': 'Tau Grade Rheostat',
    'Austenitic Manifold': 'Austenitic Manifold',
    'Dysprosium': 'Dysprosium',
    'Isotopic Coolant': 'Isotopic Coolant',
    'Reactive Gauge': 'Reactive Gauge',
    'Tungsten': 'Tungsten',
    'Caesium': 'Caesium',
    'Indicite': 'Indicite',
    'Semimetal Wafer': 'Semimetal Wafer',
    'cobalt': 'Cobalt',
    'nickel': 'Nickel',
    'ionic liquids': 'Ionic Liquids',
    'tetrafluorides': 'Tetrafluorides',
    'europium': 'Europium',
    'lithium': 'Lithium',
    'supercooled magnet': 'Supercooled Magnet',
    'tau grade rheostat': 'Tau Grade Rheostat',
    'Mag Pressure Tank': 'Mag Pressure Tank',
    'alkanes': 'Alkanes',
    'mag pressure tank': 'Mag Pressure Tank',
    'reactive gauge': 'Reactive Gauge',
    'semimetal wafer': 'Semimetal Wafer',
    'solvent': 'Solvent',
    'uranium': 'Uranium',
    'gold': 'Gold',
    'neodymium': 'Neodymium',
    'zero wire': 'Zero Wire',
    'cosmetic': 'Cosmetic',
    'fiber': 'Fiber',
    'antimony': 'Antimony',
    'vanadium': 'Vanadium',
    'palladium': 'Palladium',
    'paramagnon conductor': 'Paramagnon Conductor',
    'polymer': 'Polymer',
    'positron battery': 'Positron Battery',
    'aluminium': 'Aluminium',
    'copper': 'Copper',
    'rothicite': 'Rothicite',
    'molecular sieve': 'Molecular Sieve',
    'Sterile Nanotubes': 'Sterile Nanotubes',
    'isocentered magnet': 'Isocentered Magnet',
    'isotopic coolant': 'Isotopic Coolant',
    'tasine': 'Tasine',
    'beryllium': 'Beryllium',
    'veryl': 'Veryl',
    'ytterbium': 'Ytterbium',
    'indicite wafer': 'Indicite Wafer',
    'nuclear fuel rod': 'Nuclear Fuel Rod',
    'plutonium': 'Plutonium',
    'vytinium': 'Vytinium',
    'silver': 'Silver',
    'tantalum': 'Tantalum'
}

def map_chemical_symbols(resource):
    return RESOURCE_MAPPING.get(resource, resource)

def get_unique_resources():
    all_resources = Planets.objects.values_list('resources', flat=True)
    resource_set = set()
    for resource_list in all_resources:
        if resource_list:
            resources = resource_list.split(',')
            for resource in resources:
                resource_set.add(resource.strip())
    return sorted(resource_set)

