from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import UserShop 
from  articles.models import ArticlesPanier , Panier
from .forms import EnregistrementForm, ConnexionForm, CustomUserForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages 
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.views import PasswordResetView

# Create your views here.

def enregistrement(request):

    if request.method == 'POST':
        form = EnregistrementForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, "inscription avec success !!!")
            return redirect('index')
        
        else:
            messages.warning(request,"Informations Saisies incorrectes verifiez vos informations et mots de passes !!!")
            

    else:

        form = EnregistrementForm()

    context = {"form": form}
    return render(request, "accounts/enregistrement.html", context)

def connexion(request):
    
    if request.method == 'POST':
        form = ConnexionForm(request , data= request.POST)

        if form.is_valid() :
            user = form.get_user()
            login(request, user)
            messages.info(request, "connexion reussie !!!")

            return redirect('index')
        else:
            messages.info(request, "L'identifiant ou le mot de pass est incorrect !!!")
         
    else:

        form = ConnexionForm()

    context = {"form":form}
    return render(request, "accounts/connexion.html", context)

def deconnexion(request):

    if request.user.is_authenticated:
        Panier.objects.filter(user=request.user).delete()

    logout(request) 
    messages.info(request, "Vous êtes deconnectés !!!")

    return redirect('index')

def modifier(request):

    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            print("le formulaire est valide")
            return redirect('profil')
            
    else:
        form = CustomUserForm(instance=request.user)
        print("le formulaire n'est pas valide")

    
    context = {
        "form":form
        }
    return render(request, "articles/modifierUser.html", context)


def settings(request):


    return render(request, "accounts/settings.html")


class CustomPasswordResetView(PasswordResetView):
    html_email_template_name = 'registration/password_reset_email.html'
    email_template_name = 'registration/password_reset_email.txt'

        