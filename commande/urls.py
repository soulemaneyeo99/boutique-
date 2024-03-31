
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.list_commande),
    path('ajout_commande/', views.ajouter_commande, name="ajout_commande"),
    path('modifier_commande/<str:pk>', views.modifier_commande, name="modifier_commande"),
    path('suprimer_commande/<str:pk>', views.suprimer_commande, name="suprimer_commande")
]
