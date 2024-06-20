from django.shortcuts import render, get_object_or_404
from .models import Character, Skill

def sarah_morgan_detail(request):
    sarah = get_object_or_404(Character, id=1)
    skills = sarah.skills.all()
    return render(request, 'sarah_morgan.html', {'character': sarah, 'skills': skills})


def character_info(request):
    character_details = Character.objects.all()
    character_skills = Skill.objects.all()
    
    context = {
        'character_details': character_details,
        'character_skills': character_skills,
    }
    return render(request, 'characters/sarah_morgan.html')
