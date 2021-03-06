# Generated by Django 3.0.8 on 2020-07-26 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_advocacy_map_ov_safe_clinic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advocacy',
            options={'verbose_name': 'Advocacy Team Entry', 'verbose_name_plural': 'Advocacy Team Entries'},
        ),
        migrations.AlterModelOptions(
            name='clinical',
            options={'verbose_name': 'Clinical Team Entry', 'verbose_name_plural': 'Clinical Team Entries'},
        ),
        migrations.AlterModelOptions(
            name='map',
            options={'verbose_name': 'MAP Team Entry', 'verbose_name_plural': 'MAP Team Entries'},
        ),
        migrations.AlterModelOptions(
            name='ov',
            options={'verbose_name': 'OV Team Entry', 'verbose_name_plural': 'OV Team Entries'},
        ),
        migrations.AlterModelOptions(
            name='safe_clinic',
            options={'verbose_name': 'SAFE Clinic Team Entry', 'verbose_name_plural': 'SAFE Clinic Team Entries'},
        ),
    ]
