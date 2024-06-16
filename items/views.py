from django.shortcuts import render
from .models import ManufacturedItem

def item_search(request):
    print("Entering item_search view...")
    
    query = request.GET.get('query', '')
    print(f"Query: {query}")
    
    item_name_results = ManufacturedItem.objects.filter(item_name__icontains=query)
    print(f"Number of results: {item_name_results.count()}")
    
    context = {
        'item_name_results': item_name_results,
        'query': query,
    }
    return render(request, 'items/search_results.html', context)
