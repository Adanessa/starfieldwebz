# In tests/test_fetch_manufactured_items.py

from django.test import TestCase
from items.models import ManufacturedItem, CraftingMaterial

class FetchManufacturedItemsTestCase(TestCase):

    def setUp(self):
        # Set up any necessary data for the test (if needed)
        # For example, create some ManufacturedItem instances
        ManufacturedItem.objects.create(
            item_name="Adaptive Frame",
            work_bench="Simple Fabricator",
            special_projects_rank="",
        )
        ManufacturedItem.objects.create(
            item_name="Aldumite Drilling Rig",
            work_bench="Multiplex Fabricator",
            special_projects_rank="4",
        )

        # Create crafting materials for the items
        adaptive_frame = ManufacturedItem.objects.get(item_name="Adaptive Frame")
        CraftingMaterial.objects.create(
            manufactured_item=adaptive_frame,
            resource_name="Aluminium(Al)",
            quantity=1,
        )
        CraftingMaterial.objects.create(
            manufactured_item=adaptive_frame,
            resource_name="Iron(Fe)",
            quantity=1,
        )

        aldrumite_drilling_rig = ManufacturedItem.objects.get(item_name="Aldumite Drilling Rig")
        CraftingMaterial.objects.create(
            manufactured_item=aldrumite_drilling_rig,
            resource_name="Aldumite(Ad)",
            quantity=4,
        )
        CraftingMaterial.objects.create(
            manufactured_item=aldrumite_drilling_rig,
            resource_name="Ceasium(Cs)",
            quantity=2,
        )
        CraftingMaterial.objects.create(
            manufactured_item=aldrumite_drilling_rig,
            resource_name="Drilling Rig",
            quantity=1,
        )
        CraftingMaterial.objects.create(
            manufactured_item=aldrumite_drilling_rig,
            resource_name="Microsecond Regulator",
            quantity=1,
        )

    def test_fetch_manufactured_items(self):
        # Fetch all manufactured items
        items = ManufacturedItem.objects.all()

        # Assert that at least one item exists
        self.assertTrue(items.exists())

        # Iterate over items and verify their attributes and materials
        for item in items:
            self.assertIsNotNone(item.item_name)
            self.assertIsNotNone(item.work_bench)
            self.assertIsNotNone(item.special_projects_rank)

            # Fetch and iterate over crafting materials for the item
            materials = item.crafting_materials.all()
            for material in materials:
                self.assertIsNotNone(material.resource_name)
                self.assertGreater(material.quantity, 0)  # Ensure quantity is positive

                # Print statements (optional, for debugging or verification)
                print(f"Item: {item.item_name}, Work Bench: {item.work_bench}, Special Projects Rank: {item.special_projects_rank}")
                print(f" - Material: {material.resource_name}, Quantity: {material.quantity}")

