# Generated by Django 4.2.5 on 2023-09-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uav_management', '0003_alter_uav_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uav',
            name='weight',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
