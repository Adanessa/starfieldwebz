# Generated by Django 5.0.6 on 2024-06-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apparel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('physical', models.TextField(blank=True, null=True)),
                ('energy', models.TextField(blank=True, null=True)),
                ('em', models.TextField(blank=True, null=True)),
                ('mods', models.TextField(blank=True, null=True)),
                ('how_to_obtain', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'apparel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArmorMods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('effect', models.TextField(blank=True, null=True)),
                ('materials', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'armor_mods',
                'managed': False,
            },
        ),
    ]
