# Generated by Django 5.0.7 on 2024-07-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_recipe_recipeingredient_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
