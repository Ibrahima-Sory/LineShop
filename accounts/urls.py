from django.urls import path 
from . import views 
from accounts.views import CustomPasswordResetView

urlpatterns = [

    path("enregistrement/" , views.enregistrement , name="enregistrement" ),
    path("connexion/" , views.connexion , name="connexion" ),
    path("deconnexion/" , views.deconnexion , name="deconnexion" ),
    path("modifier/", views.modifier , name ="modifierUser"),
    path("settings/", views.settings , name= "settings"),
    #path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
   
]