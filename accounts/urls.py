from django.urls import path 
from . import views 

urlpatterns = [

    path("enregistrement/" , views.enregistrement , name="enregistrement" ),
    path("connexion/" , views.connexion , name="connexion" ),
    path("deconnexion/" , views.deconnexion , name="deconnexion" ),
    
   
]