from django.db import models

class Client(models.Model):
    Nom = models.CharField(max_length=200, null=True)
    Telephone  = models.CharField(max_length=50, null=True)
    Date_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Nom if self.Nom else ''

