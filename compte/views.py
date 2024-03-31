from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .form import CreerUtilisateur


# Create your views here.
def inscriptionPage(request):
    form = CreerUtilisateur()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Compte créé avec succès pour  ' + user)
            return redirect('accès')

    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


def accèsPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.info(request, "Nom d'utilisateur et/ou mot de passe incorrect")

    return render(request, 'compte/accès.html', context)


def logoutUser(request):
    logout(request)
    return redirect('accès')
