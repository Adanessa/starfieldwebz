from django.db import models

class Planets(models.Model):
    system = models.ForeignKey('Systems', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    gravity = models.CharField(max_length=50, blank=True, null=True)
    temperature = models.CharField(max_length=50, blank=True, null=True)
    atmosphere = models.CharField(max_length=50, blank=True, null=True)
    magnetosphere = models.CharField(max_length=50, blank=True, null=True)
    water = models.CharField(max_length=50, blank=True, null=True)
    biomes = models.TextField(blank=True, null=True)
    traits = models.TextField(blank=True, null=True)
    fauna = models.TextField(blank=True, null=True)
    flora = models.TextField(blank=True, null=True)
    resources = models.TextField(blank=True, null=True)
    planet_length = models.CharField(max_length=50, blank=True, null=True)
    domesticable = models.TextField(blank=True, null=True)
    hab_rank = models.TextField(blank=True, null=True)
    gatherable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planets'
        
    def __str__(self):
        return self.name
        
        
class Systems(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    system_resources = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'systems'
        
    def __str__(self):
        return self.name
    
class ManufacturedItem(models.Model):
    item_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'items_manufactureditem'

    def __str__(self):
        return self.item_name
    
class CraftingMaterial(models.Model):
    manufactured_item = models.ForeignKey(ManufacturedItem, related_name='crafting_materials', on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'items_craftingmaterial'

    def __str__(self):
        return self.resource_name

