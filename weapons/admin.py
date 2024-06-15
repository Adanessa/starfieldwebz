from django.contrib import admin

from .models import AidItems, Weapons, AllWeaponModPrefixes, AllWeaponPerks

admin.site.register(AidItems)
admin.site.register(Weapons)
admin.site.register(AllWeaponModPrefixes)
admin.site.register(AllWeaponPerks)