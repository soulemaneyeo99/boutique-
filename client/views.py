from django.shortcuts import render, redirect
from django.http import HttpResponse
from commande.forms import CommandeForm
from .forms import ClientForm
from .models import Client


def list_client(request, pk):
    """
    Affiche les informations sur un client et ses commandes associées.
    """
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()
    context = {'client': client, 'commande': commande, 'commande_total': commande_total}
    return render(request, 'client/list_client.html', context)


def ajouter_client(request):
    """
    Affiche le formulaire pour ajouter un client.
    """
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'client/ajouter_client.html', context)


def modifier_client(request, pk):
    """
    Affiche le formulaire pour modifier les informations d'un client.
    """
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'client/ajouter_client.html', context)


def suprimer_client(request, pk):
    """
    Supprime un client.
    """
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/')
    context = {'item': client}
    return render(request, 'client/suprimer_client.html', context)
