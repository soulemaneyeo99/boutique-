from django.shortcuts import render

def liste_projets(request):
    # Exemple de données pour tester
    projets = [
        {'id': 1, 'nom': 'Projet Alpha', 'description': 'Description du projet Alpha'},
        {'id': 2, 'nom': 'Projet Beta', 'description': 'Description du projet Beta'},
    ]
    return render(request, 'projet/liste_projets.html', {'projets': projets})

def detail_projet(request, id):
    # Exemple de données pour tester
    projet = {'id': id, 'nom': 'Projet Alpha', 'description': 'Description du projet Alpha'}
    return render(request, 'projet/detail_projet.html', {'projet': projet})
