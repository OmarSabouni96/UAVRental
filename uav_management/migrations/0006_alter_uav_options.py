# Generated by Django 4.2.5 on 2023-09-25 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uav_management', '0005_alter_uav_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uav',
            options={'ordering': ['-created']},
        ),
    ]
