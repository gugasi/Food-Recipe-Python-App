# Generated by Django 4.2.1 on 2023-06-04 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_recipe_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipe_images'),
        ),
    ]
