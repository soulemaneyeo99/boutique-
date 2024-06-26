# Generated by Django 5.0.2 on 2024-02-27 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_rename_product_produit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='date_debut',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='tag',
            field=models.ManyToManyField(to='produit.tag'),
        ),
    ]
