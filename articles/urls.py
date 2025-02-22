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
    path("panier/valider/", views.validerPanier, name="validerPanier"),
    path("panier/valider/commmande/<int:id>/", views.commande, name="commande"),
    path("panier/valider/commmande/historique/", views.histCommande, name="histCommande"),
    path("remove/<int:idSup>/" , views.supPanier , name="supPanier"),
    path("recherche/", views.recherche , name="recherche"),
    path("gestion/", views.gestion , name="gestion"),
    path("gestionE/", views.gestionE , name="gestionE"),
    path("gestionM/", views.gestionM , name="gestionM"),
    path("gestionTelephone/", views.gestionTelephone , name="gestionTelephone"),
    path("gestionOrdi/", views.gestionOrdi , name="gestionOrdi"),
    path("gestionCasque/", views.gestionCasque , name="gestionCasque"),
    path("gestionAirpods/", views.gestionAirpods , name="gestionAirpods"),
    path("gestionMontre/", views.gestionMontre , name="gestionMontre"),
    path("gestionShoes/", views.gestionShoes , name="gestionShoes"),
    path("gestionHabits/", views.gestionHabits , name="gestionHabits"),
    path("gestionAccessoires/", views.gestionAccessoires , name="gestionAccessoires"),
    path("rechercheG/", views.rechercheG , name="rechercheG"),
    path("gestion/ajouter", views.ajouter , name="ajouter"),
    path("gestion/modifier/<int:idArt>/", views.modifierArt , name="modifierArt"),
    path("gestion/supprimer/<int:idArt>/", views.supArticle , name="supArticle"),


    
   
]
