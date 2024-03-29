from django.db import models

class Tag(models.Model):
    Nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Nom if self.Nom else ''

class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prix = models.FloatField(null=True)
    nombre = models.CharField(max_length=200, null=True)
    date_debut = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.nom if self.nom else ''
