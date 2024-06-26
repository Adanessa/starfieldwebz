from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    faction = models.CharField(blank=True, null=True)
    image_filename = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = False
        db_table = 'characters_character'
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    character = models.ForeignKey(Character, related_name='skills', on_delete=models.CASCADE)
    
    class Meta:
        managed = False
        db_table = 'characters_skill'