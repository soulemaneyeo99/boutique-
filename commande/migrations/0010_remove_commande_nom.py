# Generated by Django 5.0.2 on 2024-03-03 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0009_commande_nom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='Nom',
        ),
    ]