# Generated by Django 5.0.7 on 2024-08-18 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_rename_item_college'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='name',
            new_name='collage_name',
        ),
    ]
