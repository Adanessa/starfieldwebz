from django.shortcuts import render
from .models import ManufacturedItem

def item_search(request):
    query = request.GET.get('query', '')
    item_name_results = ManufacturedItem.objects.filter(item_name__icontains=query)
    context = {
        'item_name_results': item_name_results,
        'query': query,
    }
    return render(request, 'items/search_results.html', context)