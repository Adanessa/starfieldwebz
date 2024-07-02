from .models import Planets

# Mapping of resource abbreviations to standardized names
RESOURCE_MAPPING = {
    'Fe': 'Fe',
    'Iron': 'Fe',
    'Iron(Fe)': 'Fe',
    'He-3': 'He-3',
    'Al': 'Al',
    'Aluminium': 'Al',
    'Aluminium(Al)': 'Al',
    'Be': 'Be',
    'Beryllium': 'Be',
    'Eu': 'Eu',
    'Europium': 'Eu',
    'Cl': 'Cl',
    'Chlorine': 'Cl',
    'H2O': 'H2O',
    'Water': 'H2O',
    'Li': 'Li',
    'Lithium': 'Li',
    'Ag': 'Ag',
    'Silver': 'Ag',
    'Cu': 'Cu',
    'Copper': 'Cu',
    'Cs': 'Cs',
    'Caesium': 'Cs',
    'Cs': 'Cs',
    'Caesium': 'Cs',
    'Ceasium(Cs)': 'Cs',
    'Fiber': 'Fiber',
    'Nutrient': 'Nutrient',
    'Sealant': 'Sealant',
    'Structural Material': 'Structural Material',
    'Pb': 'Pb',
    'Lead': 'Pb',
    'Ni': 'Ni',
    'Nickel': 'Ni',
    'Nickel(Ni)': 'Ni',
    'U': 'U',
    'Uranium': 'U',
    'Pu': 'Pu',
    'Plutonium': 'Pu',
    'F': 'F',
    'Fluorine': 'F',
    'Ag': 'Ag',
    'Silver': 'Ag',
    'Hg': 'Hg',
    'Mercury': 'Hg',
    'Aluminium(Al)': 'Aluminium',
    'Iron(Fe)': 'Iron',
    'Aldumite(Ad)': 'Aldumite',
    'Ceasium(Cs)': 'Ceasium',
    'Drilling Rig': 'Drilling Rig',
    'Microsend Regulator': 'Microsend Regulator',
    'Isocentered Magnet': 'Isocentered Magnet',
    'Tau Grade Rheostat': 'Tau Grade Rheostat',
    'Austenitic Manifold': 'Austenitic Manifold',
    'Dysprosium': 'Dysprosium',
    'Isotopic Coolant': 'Isotopic Coolant',
    'Reactive Gauge': 'Reactive Gauge',
    'Tungsten': 'Tungsten',
    'Caesium': 'Ceasium',
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

# Mapping to display full name of resources
RESOURCE_DISPLAY_MAPPING = {
    'Ad': 'Aldumite(Ad)',
    'Ag': 'Silver(Ag)',
    'Al': 'Aluminium(Al)',
    'Aq': 'Aqueous Hematite(Aq)',
    'Ar': 'Argon(Ar)',
    'Au': 'Gold(Au)',
    'Be': 'Beryllium(Be)',
    'Cl': 'Chlorine(Cl)',
    'Co': 'Cobalt(Co)',
    'Cs': 'Ceasium(Cs)',
    'Ct': 'Caelumite(Ct)',
    'C6Hn': 'Benzene(C6Hn)',
    'Cu': 'Copper(Cu)',
    'Dy': 'Dysposium(Dy)',
    'Eu': 'Europium(Eu)',
    'F': 'Fluorine(F)',
    'Fe': 'Iron(Fe)',
    'He-3': 'Helium-3(He-3)',
    'Hg': 'Mercury(Hg)',
    'HnCn': 'Alkanes(HnCn)',
    'H2O': 'Water(H₂O)',
    'Ie': 'Indicite(Ie)',
    'IL': 'Ionic Liquids(IL)',
    'Ir': 'Iridium(Ir)',
    'Li': 'Lithium(Li)',
    'Nd': 'Neodymium(Nd)',
    'Ne': 'Neon(Ne)',
    'Ni': 'Nickel(Ni)',
    'Pb': 'Lead(Pb)',
    'Pd': 'Palladium(Pd)',
    'Pt': 'Platinum(Pt)',
    'Pu': 'Plutonium(Pu)',
    'R-COOH': 'Carboxylic Acids(R-COOH)',
    'Rc': 'Rothicite(Rc)',
    'Sb': 'Antimony(Sb)',
    'SiH3Cl': 'Chlorosilanes(SiH₃Cl)',
    'Ta': 'Tantalum(Ta)',
    'Ti': 'Titanium(Ti)',
    'Tsn': 'Tasine(Tsn)',
    'U': 'Uranium(U)',
    'V': 'Vanadium(V)',
    'Vr': 'Veryl(Vr)',
    'Vy': 'Vytinium(Vy)',
    'W': 'Tungsten(W)',
    'Xe': 'Xenon(Xe)',
    'xF4': 'Tetrafluorides(xF4)',
    'Yb': 'Ytterbium(Yb)',
}

def map_chemical_symbols(resource):
    return RESOURCE_MAPPING.get(resource, resource)

def map_display_names(resource):
    return RESOURCE_DISPLAY_MAPPING.get(resource, resource)

# Function to retrive unoque resources from database and categorize them as inorganic or organic.
def get_unique_resources():
    all_resources = Planets.objects.values_list('resources', flat=True)
    inorganic_resources = []
    organic_resources = []

    # Identifiers for categorizing resources
    inorganic_identifiers = {
        'Ad','Ag', 'Al', 'Aq', 'Ar', 'Au', 'Be', 'Cl', 'Co', 'Cs', 'Ct',
        'C6Hn', 'Cu', 'Dy', 'Eu', 'F', 'Fe', 'He-3', 'Hg', 'HnCn', 'H2O', 'Ie',
        'IL', 'Ir', 'Li', 'Nd', 'Ne', 'Ni', 'Pb', 'Pd', 'Pt', 'Pu', 'R-COOH',
        'Rc', 'Sb', 'SiH3Cl', 'Ta', 'Ti', 'Tsn', 'U', 'V', 'Vr', 'Vy', 'W', 'Xe',
        'xF4', 'Yb'
        }
    organic_identifiers = {
        'Adhesive', 'Aromatic', 'Cosmetic', 'Fiber'
    }

    for resource_list in all_resources:
        if resource_list:
            resources = resource_list.split(',')
            for resource in resources:
                cleaned_resource = resource.strip()

                # Check if the resource name matches any inorganic identifier
                if any(identifier in cleaned_resource for identifier in inorganic_identifiers):
                    inorganic_resources.append(cleaned_resource)
                # Check if the resource name matches any organic identifier
                elif any(identifier in cleaned_resource for identifier in organic_identifiers):
                    organic_resources.append(cleaned_resource)
                # Default to organic if not matched as organic
                else:
                    organic_resources.append(cleaned_resource)
    return {
        'inorganic_resources': sorted(set(inorganic_resources)),
        'organic_resources': sorted(set(organic_resources))
    }

