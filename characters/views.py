from django.shortcuts import render, get_object_or_404
from .models import Character, Skill

def sarah_morgan_detail(request):
    sarah = get_object_or_404(Character, id=1)
    skills = sarah.skills.all()
    return render(request, 'sarah_morgan.html', {'character': sarah, 'skills': skills})

def andreja_detail(request):
    andreja = get_object_or_404(Character, id=4)
    skills = andreja.skills.all()
    return render(request, 'andreja.html', {'character': andreja, 'skills': skills})

def amundsen_barret(request):
    amundsen_barret = get_object_or_404(Character, id=2)
    skills = amundsen_barret.skills.all()
    return render(request, 'amundsen_barret.html', {'character': amundsen_barret, 'skills': skills})

def same_coe(request):
    same_coe = get_object_or_404(Character, id=3)
    skills = same_coe.skills.all()
    return render(request, 'sam_coe.html', {'character': same_coe, 'skills': skills})

def heller(request):
    heller = get_object_or_404(Character, id=5)
    skills = heller.skills.all()
    return render(request, 'heller.html', {'character': heller, 'skills': skills})
# def character_info(request):
#     character_details = Character.objects.all()
#     character_skills = Skill.objects.all()
    
#     context = {
#         'character_details': character_details,
#         'character_skills': character_skills,
#     }
#     return render(request, {'sarah_morgan.html', 'andreja.html'})
