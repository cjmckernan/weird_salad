# Generated by Django 5.0.7 on 2024-07-17 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('stock', '0003_recipe_cost'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recipe',
            unique_together={('name', 'location')},
        ),
    ]
