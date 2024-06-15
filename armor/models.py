from django.db import models

class Apparel(models.Model):
    name = models.TextField(blank=True, null=True)
    physical = models.TextField(blank=True, null=True)
    energy = models.TextField(blank=True, null=True)
    em = models.TextField(blank=True, null=True)
    mods = models.TextField(blank=True, null=True)
    how_to_obtain = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apparel'
        
class ArmorMods(models.Model):
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    materials = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'armor_mods'