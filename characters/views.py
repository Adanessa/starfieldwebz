from django.shortcuts import render, get_object_or_404
from .models import Character

def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'character_detail.html', {'character': character})
