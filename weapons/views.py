from django.shortcuts import render
from .models import Weapons, AllWeaponModPrefixes, AllWeaponPerks

def weapon_search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        weapons = Weapons.objects.filter(name__icontains=query)     #Filter by name
        
        context = {
            'weapons': weapons,
            'query': query,
        }
        return render(request, 'weapons/search_results.html', context)
    
def display_all_items(request):