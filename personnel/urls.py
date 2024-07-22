from django.urls import path
from . import views

urlpatterns = [
    path("inscription/", views.index),
    path("connexion/", views.cnxprestataire),
    path("postuler/", views.postuler),
    path("profil/", views.pflprestataire),
    path("editer-compte/", views.edtcompte),
    path("administrateur/connexion/", views.connexion),
    path("administrateur/candidatures/", views.candidatures),
    path("administrateur/candidature/", views.candidature),
    path("administrateur/comptes/", views.comptes),
    path("administrateur/ajouter-compte/", views.ajtcompte),
    path("administrateur/projets/", views.projets),
    path("administrateur/ajouter-projet/", views.ajtprojet),
    path("administrateur/editer-compte/", views.edtcompte),
    path("administrateur/profil/", views.profil),
]
