# Generated by Django 5.0.2 on 2024-02-27 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='Address',
            new_name='Telephone',
        ),
    ]