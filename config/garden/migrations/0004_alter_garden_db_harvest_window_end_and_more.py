# Generated by Django 4.2.4 on 2023-08-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0003_alter_garden_db_seed_depth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden_db',
            name='harvest_window_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='garden_db',
            name='harvest_window_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='garden_db',
            name='sow_window_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='garden_db',
            name='sow_window_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='garden_db',
            name='transplant_window_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='garden_db',
            name='transplant_window_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]