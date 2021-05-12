# Generated by Django 3.1.3 on 2021-01-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0017_auto_20210115_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocacy',
            name='emp_name',
            field=models.TextField(default='Enter your name here', max_length=50, verbose_name='Employee Name'),
        ),
        migrations.AlterField(
            model_name='clinical',
            name='emp_name',
            field=models.TextField(default='Enter your name here', max_length=50, verbose_name='Employee Name'),
        ),
        migrations.AlterField(
            model_name='clinical_voca',
            name='emp_name',
            field=models.TextField(default='Enter your name here', max_length=50, verbose_name='Employee Name'),
        ),
        migrations.AlterField(
            model_name='map',
            name='emp_name',
            field=models.TextField(default='Enter your name here', max_length=50, verbose_name='Employee Name'),
        ),
        migrations.AlterField(
            model_name='ov',
            name='emp_name',
            field=models.TextField(default='Enter your name here', max_length=50, verbose_name='Employee Name'),
        ),
        migrations.AlterField(
            model_name='safe_clinic',
            name='emp_name',
            field=models.TextField(default='Enter your name here', max_length=50, verbose_name='Employee Name'),
        ),
    ]