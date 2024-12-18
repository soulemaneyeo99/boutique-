
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('<str:pk>', views.list_client,name='client'),
    path('modifier_client/<int:pk>/', views.modifier_client, name='modifier_client'),
    path('suprimer_client/<int:pk>/', views.suprimer_client, name='suprimer_client'),

]
