
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('inscription', views.inscriptionPage,name='inscription'),
    path('accès', views.accèsPage,name='accès'),
    path('Quitter', views.logoutUser,name='Quitter'),

]
