from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index , name="index" ),
    path("electroniques/", views.electroniques , name="electroniques"),
    path("modes/", views.modes , name="modes"),
    path("promo/", views.promo , name="promo"),
    path("add/<int:idAjout>/", views.ajoutPanier , name="ajoutPanier" ),
    path("<int:idDetail>/", views.details , name="details"),
    path("modals/", views.modals , name="modals"),
    path("profil/", views.profil , name="profil"),
    path("panier/" , views.panier , name="panier"),
    path("panier/change_quantite/", views.change_quantite, name="change_quantite"),
    path("remove/<int:idSup>/" , views.supPanier , name="supPanier"),
    path("recherche/", views.recherche , name="recherche"),
    path("achat/<int:idAchat>/", views.achat , name="achat"),
    path("gestion/", views.gestion , name="gestion"),
    path("gestionE/", views.gestionE , name="gestionE"),
    path("gestionM/", views.gestionM , name="gestionM"),
    path("rechercheG/", views.rechercheG , name="rechercheG"),
    path("gestion/ajouter", views.ajouter , name="ajouter"),
    path("gestion/modifier/<int:idArt>/", views.modifierArt , name="modifierArt"),
    path("gestion/supprimer/<int:idArt>/", views.supArticle , name="supArticle"),


    
   
]
