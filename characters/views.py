from django.shortcuts import render, get_object_or_404
from .models import Character

def sarah_morgan_detail(request):
    sarah = get_object_or_404(Character, id=1)
    return render(request, 'sarah_morgan.html', {'character': sarah})
