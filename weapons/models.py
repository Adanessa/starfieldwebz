# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AidItems(models.Model):
    name = models.TextField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aid_items'


class AllMissionboardMissions(models.Model):
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    system = models.TextField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    how_to_get = models.TextField(db_column='How to Get', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'all_missionboard_missions'


class AllPerkPrefixes(models.Model):
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_perk_prefixes'


class AllWeaponModPrefixes(models.Model):
    name = models.TextField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_weapon_mod_prefixes'


class AllWeaponPerks(models.Model):
    name = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_weapon_perks'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bays(models.Model):
    name = models.TextField(blank=True, null=True)
    brands = models.TextField(blank=True, null=True)
    mass = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    requires = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bays'


class CargoHolds(models.Model):
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    cargo = models.IntegerField(blank=True, null=True)
    hull = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    mass = models.IntegerField(blank=True, null=True)
    cargo_mass_ratio = models.TextField(blank=True, null=True)
    shielded = models.TextField(blank=True, null=True)
    required = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo_holds'


class Cockpits(models.Model):
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    cargo = models.IntegerField(blank=True, null=True)
    hull = models.IntegerField(blank=True, null=True)
    crew_stations = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    mass = models.IntegerField(blank=True, null=True)
    required = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cockpits'


class CookingStation(models.Model):
    name = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    materials = models.TextField(blank=True, null=True)
    required_research = models.TextField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cooking_station'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Engines(models.Model):
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    max_power = models.IntegerField(blank=True, null=True)
    engine_thrust = models.IntegerField(blank=True, null=True)
    maneuvering_thrust = models.IntegerField(blank=True, null=True)
    engine_health = models.IntegerField(blank=True, null=True)
    crew_capacity = models.FloatField(blank=True, null=True)
    hull = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    mass = models.IntegerField(blank=True, null=True)
    requires = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engines'


class FuelTanks(models.Model):
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    grav_jump_fuel = models.IntegerField(blank=True, null=True)
    fuel_mass_ratio = models.FloatField(blank=True, null=True)
    hull = models.IntegerField(blank=True, null=True)
    mass = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    requires = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuel_tanks'


class GravDrives(models.Model):
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    max_power = models.IntegerField(blank=True, null=True)
    grav_jump_thrust = models.IntegerField(blank=True, null=True)
    grav_drive_health = models.IntegerField(blank=True, null=True)
    mass = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    requires = models.TextField(blank=True, null=True)
    starship_design_rank = models.IntegerField(blank=True, null=True)
    hull = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grav_drives'


class Habs(models.Model):
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    passenger_slots = models.IntegerField(blank=True, null=True)
    hull = models.IntegerField(blank=True, null=True)
    mass = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    requires = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habs'


class LandingGears(models.Model):
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    landing_thrust = models.IntegerField(blank=True, null=True)
    hull = models.IntegerField(blank=True, null=True)
    mass = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    requires = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'landing_gears'


class PharmaceuticalLab(models.Model):
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    materials = models.TextField(blank=True, null=True)
    required_research = models.TextField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmaceutical_lab'


class Powers(models.Model):
    name = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'powers'



class Weapons(models.Model):
    name = models.TextField(blank=True, null=True)
    rarity = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    dmg = models.TextField(blank=True, null=True)
    ammo = models.TextField(blank=True, null=True)
    mag = models.TextField(blank=True, null=True)
    fire_rate = models.TextField(blank=True, null=True)
    range = models.TextField(blank=True, null=True)
    accuracy = models.TextField(blank=True, null=True)
    mass = models.TextField(blank=True, null=True)
    mod_capacity = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weapons'
