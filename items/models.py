from django.db import models

class ManufacturedItem(models.Model):
    item_name = models.CharField(max_length=100)
    work_bench = models.CharField(max_length=100)
    special_projects_rank = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.item_name

class CraftingMaterial(models.Model):
    manufactured_item = models.ForeignKey(ManufacturedItem, related_name='crafting_materials', on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.resource_name} ({self.quantity})"
