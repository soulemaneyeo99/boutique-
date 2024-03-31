from django.db import models
from client.models import Client
from produit.models import Produit

class Commande(models.Model):
    STATUS = (('en instance', 'en instance'),
        ('non livré', 'non livré'),
        ('livré', 'Livré'))
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,null=True, choices=STATUS)
    date_commande = models.DateTimeField(auto_now=True)
