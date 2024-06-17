from django.shortcuts import render
from .models import Weapons, AllWeaponModPrefixes, AllWeaponPerks

def weapon_search(request):
    query = request.GET.get('query', '')
    weapons = Weapons.objects.filter(name__icontains=query)
    context = {
        'weapons': weapons,
        'query': query,
    }
    return render(request, 'weapons/search_results.html', context)
    
def display_all_weapons(request):
    weapons = Weapons.objects.all()
    weapon_mod_prefixes = AllWeaponModPrefixes.objects.all()
    weapon_perks = AllWeaponPerks.objects.all()
    
    context = {
        'weapons': weapons,
        'weapon_mod_prefixes': weapon_mod_prefixes,
        'weapon_perks': weapon_perks,
    }
    return render(request, 'weapons/display_all_weapons.html', context)