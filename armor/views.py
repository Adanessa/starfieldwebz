from django.shortcuts import render
from .models import Apparel, ArmorMods

def display_all_armor_stuff(request):
    apparel = Apparel.objects.all()
    armor_mods = ArmorMods.objects.all()
    
    context = {
        'apparel': apparel,
        'armor_mods': armor_mods,
    }
    return render(request, 'armor/display_all_armor_stuff.html', context)