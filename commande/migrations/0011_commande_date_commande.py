# Generated by Django 5.0.2 on 2024-03-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0010_remove_commande_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='date_commande',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
