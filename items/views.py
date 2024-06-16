from django.shortcuts import render
from .models import ManufacturedItem, CraftingMaterial

def gather_materials(item_name, multiplier=1):
    materials_needed = {}
    processed_items = set()
    
    def find_item(item_name):
        try:
            return ManufacturedItem.objects.get(item_name__iexact=item_name)
        except ManufacturedItem.DoesNotExist:
            return None
        
    def inner_gather_materials(item_name, multiplier):
        item = find_item(item_name)
        if not item:
            return
        
        for material in item.crafting_materials.all():
            resource_name = material.resource_name
            quantity = material.quantity * multiplier
            
            materials_needed[resource_name] = materials_needed.get(resource_name, 0) + quantity
            
            if resource_name not in processed_items:
                processed_items.add(resource_name)
                inner_gather_materials(resource_name, quantity)
                
    inner_gather_materials(item_name, multiplier)
    return materials_needed

def search_items(request):
    if request.method == 'GET':
        item_names = request.GET.get('items', '').split(',')
        item_names = [name.strip() for name in item_names]
        
        total_materials_needed = {}
        for item_name in item_names:
            materials_needed = gather_materials(item_name)
            for material, quantity in materials_needed.items():
                total_materials_needed[material] = total_materials_needed.get(material, 0) + quantity
                
        return render(request, 'items/search_results.html', {
            'materials_needed': total_materials_needed
        })
    return render(request, 'items/search_form.html')