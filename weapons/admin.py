from django.contrib import admin

from .models import AidItems, Weapons, AllWeaponModPrefixes, AllWeaponPerks

admin.site.register(AidItems)
admin.site.register(AllWeaponModPrefixes)
admin.site.register(AllWeaponPerks)

class WeaponsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'type', 'dmg', 'ammo', 'mag', 'fire_rate', 'range', 'accuracy', 'mass', 'mod_capacity', 'image_filename')

admin.site.register(Weapons, WeaponsAdmin)