from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'inscription.html')

def cnxprestataire(request):
    return render(request, "cnx-prestataire.html")

def postuler(request):
    return render(request, "postuler.html")

def connexion(request):
    return render(request, "connexion.html")

def candidatures(request):
    return render(request, "candidatures.html")

def candidature(request):
    return render(request, "candidature.html")

def comptes(request):
    return render(request, "comptes.html")

def ajtcompte(request):
    return render(request, "ajouter-compte.html")

def projets(request):
    return render(request, "projets.html")

def ajtprojet(request):
    return render(request, "ajouter-projet.html")

def edtcompte(request):
    return render(request, "editer-compte.html")

def profil(request):
    return render(request, "profil.html")

def pflprestataire(request):
    return render(request, "pfl-prestataire.html")