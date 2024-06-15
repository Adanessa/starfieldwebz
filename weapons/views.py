from django.shortcuts import render
from .models import Weapons

def weapon_search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        weapons = Weapons.objects.filter(name__icontains=query)     #Filter by name
        
        context = {
            'weapons': weapons,
            'query': query,
        }
        return render(request, 'app_boss/search_results.html', context)