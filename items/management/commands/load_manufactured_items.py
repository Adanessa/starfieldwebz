import json
import os
from django.core.management.base import BaseCommand
from items.models import ManufacturedItem, CraftingMaterial

class Command(BaseCommand):
    help = 'Load manufactured items from a JSON file'

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(__file__), 'manufactured_items.json')

        with open(file_path, 'r') as file:
            data = json.load(file)

        for item in data['manufactured_items']:
            manufactured_item = ManufacturedItem.objects.create(
                item_name=item['item_name'],
                work_bench=item['work_bench'],
                special_projects_rank=item.get('special_projects_rank', '')
            )

            for material in item['crafting_materials']:
                CraftingMaterial.objects.create(
                    manufactured_item=manufactured_item,
                    resource_name=material['resource_name'],
                    quantity=material['quantity']
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded manufactured items.'))
