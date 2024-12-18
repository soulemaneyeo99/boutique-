from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('commande/', include('commande.urls')),  # URL pour l'application commande
    path('client/', include('client.urls')),      # URL pour l'application client
    path('produit/', include('produit.urls')),  
    path('compte/', include('compte.urls')),      # URL pour l'application projet
      
]
