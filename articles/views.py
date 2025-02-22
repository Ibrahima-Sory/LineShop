from django.shortcuts import render , get_object_or_404 ,redirect 
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Categories , Articles , Panier,ArticlesPanier, Annonces , AchatPanier
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import ArticlesForms


# Create your views here.

def index(request):
    articles = Articles.objects.all()
    #achatarticle = AchatArticle.objects.all()
    electroniques = Articles.objects.filter(categorie__name='Electroniques')
    modes = Articles.objects.filter(categorie__name='Modes')
    annonce1 = Annonces.objects.filter(titre ='promo1')
    annonce2 = Annonces.objects.filter(titre ='promo2')

    articlesPanier = ArticlesPanier.objects.all()
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1

    context = {
        "articles":articles,
        #"achat":achatarticle,
        "electroniques":electroniques,
        "modes":modes,
        "annonce1":annonce1,
        "annonce2":annonce2,
        "nbrArt":nbrArt
    }
         
    return render(request, "articles/index.html" , context)

def modals(request):
    articles = get_object_or_404(Articles)
    context = {
        "articles":articles,
        
    }

    return render(request, "articles/modal.html", context)

def profil (request):
    if request.user.is_authenticated :
        articlesPanier = ArticlesPanier.objects.all()
        nbrArt = 0
        for article in articlesPanier:
            nbrArt += 1

        context = {
            'nbrArt':nbrArt,
        }

        return render(request, "articles/profil.html", context)
    else:
        return redirect('enregistrement')
    

def details(request, idDetail):
    articles = get_object_or_404(Articles, id = idDetail)

    articlesPanier = ArticlesPanier.objects.all()
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1

    context = {
        "articles":articles,
        "nbrArt": nbrArt,
        
    }

    return render(request, "articles/details.html", context)


def electroniques(request):
    articles = Articles.objects.all()
    electroniques = Articles.objects.filter(categorie__name='Electroniques')
    telephones = Articles.objects.filter(type = 'Telephone')
    ordinateurs = Articles.objects.filter(type = 'Ordinateurs')
    montres = Articles.objects.filter(type = 'Montres')
    airpods = Articles.objects.filter(type = 'Airpods')
    casques = Articles.objects.filter(type = 'Casques')
    annonce2 = Annonces.objects.filter(titre ='promo2')

    articlesPanier = ArticlesPanier.objects.all()
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1

    context = {
        "articles":articles,
        "electroniques":electroniques,
        "telephones":telephones,
        "ordinateurs":ordinateurs,
        "montres":montres,
        "airpods":airpods,
        "casques":casques,
        "annonce2":annonce2,
        "nbrArt":nbrArt,
    }

    return render(request, "articles/electroniques.html" , context )

def modes(request):
    articles = Articles.objects.all()
    modes = Articles.objects.filter(categorie__name='Modes')
    shoes = Articles.objects.filter(type = 'Shoes')
    habits = Articles.objects.filter(type = 'Habits')
    accessoires = Articles.objects.filter(type = 'Accessoires')
    annonce1 = Annonces.objects.filter(titre ='promo1')

    articlesPanier = ArticlesPanier.objects.all()
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1

    context = {
        "articles":articles,
        "modes":modes,
        "shoes":shoes,
        "habits":habits,
        "accessoires":accessoires,
        "annonce1":annonce1,
        "nbrArt":nbrArt,
    }

    return render(request, "articles/modes.html" , context )

def promo(request):
    articles_enpromo = Articles.objects.filter(enpromo = True)
    articles_enpromo_electro = Articles.objects.filter(enpromo = True , categorie__name='Electroniques')
    articles_enpromo_mode = Articles.objects.filter(enpromo =True , categorie__name='Modes')

    articlesPanier = ArticlesPanier.objects.all()
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1

    context = {
        "articles": articles_enpromo,
        "electroniques": articles_enpromo_electro,
        "modes": articles_enpromo_mode,
        "nbrArt":nbrArt,
    }
    return render(request,"articles/promo.html" ,context)
    


def panier(request):
    articlesPanier = ArticlesPanier.objects.all()
    prixTotal = sum( (article.article.prix_promo if article.article.enpromo  else article.article.prix ) * article.quantite for article in articlesPanier )
    #if request.user.is_authenticated:
    #    nbrArt = ArticlesPanier.total_articles(request.user)
    #else:
    #    nbrArt = 0
    #print(f"{articlesPanier}____________")
    #articlesPanier = ArticlesPanier.objects.all()
    #prixTotalP = sum( (article.article.prix_promo if article.article.enpromo  else article.article.prix ) * article.quantite for article in articlesPanier )
    panier = Panier
    prix= panier.prixTotal = prixTotal
    #panier.save()


    def prixTotal_formater():
        return f"{prix:,.0f}".replace(",", " ")
    
    nbrArtTotal = sum(article.quantite for article in articlesPanier)
    
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1

    context = {
        'articlesPanier':articlesPanier,
        'prixTotal':prixTotal_formater,
        'nbrArtTotal':nbrArtTotal,  
        'nbrArt':nbrArt,  
    }
    

    return render(request, "articles/panier.html" , context)



def ajoutPanier( request, idAjout ):
    
    if request.user.is_authenticated:
        article = Articles.objects.get(id=idAjout)
        panier , created = Panier.objects.get_or_create( user = request.user)
        articlePanier , created = ArticlesPanier.objects.get_or_create(article = article , panier=panier )
        #<input type="number" action="{% url 'ajoutPanier' article.id %}" name="quantite" value="1" min="1">
        #return redirect('panier')

        if request.method == "POST":
            data = json.loads(request.body)
            
            quantite = data["quantite"]
            articlePanier.quantite = quantite
            articlePanier.save()
            

            messages.success(request, "L'article a été ajouté au panier avec succès!") 


                # Récupérer les messages
            #message_list = []
            #for message in messages.get_messages(request):
                #message_list.append({
                    #'level': message.tags,
                    #'message': message.message
                #})    


            return JsonResponse({'success': True, }) 
    else:    
        messages.info(request, "Vous devez être connecté pour ajouter des articles au panier.")
        return JsonResponse({'success': False, })
        
    if articlePanier.quantite <= 1 :   
        articlePanier.quantite += 1
  
        
        articlePanier.save()

        #return redirect('panier') 
        #return render(request, 'articles/index.html') 
        #return  JsonResponse({'success': True})

    else:
        messages.info(request, "Vous devez être connecté pour ajouter des articles au panier.")
        return redirect('connexion')

def supPanier(request, idSup ):
    articlePanier = ArticlesPanier.objects.get(id=idSup)
    articlePanier.delete()

    return redirect('panier')

def change_quantite(request):
    if request.method == "POST":
        data = json.loads(request.body)
        articlePanierId = data["article_id"]
        quantite = data["quantite"]

        panierUser = Panier.objects.get(user= request.user)
        articlePanier = get_object_or_404(ArticlesPanier,id= articlePanierId, panier= panierUser)
        articlePanier.quantite = quantite
        articlePanier.save()

        articlesPanier = ArticlesPanier.objects.all()
        prixTotal = sum( (article.article.prix_promo if article.article.enpromo  else article.article.prix ) * article.quantite for article in articlesPanier )
#        articlesPanier.save()
#        Panier.prixTotal = prixTotalP
#        Panier.save()

        def prixTotal_formater():
           return f"{prixTotal:,.0f}".replace(",", " ")
        
        
        return JsonResponse({'success': True , 'prixTotal': prixTotal_formater() })

    return JsonResponse({'success':False}, status = 400)

def recherche(request):
    recherche = request.GET.get('r')
    resultats = []

    articlesPanier = ArticlesPanier.objects.all()
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1

    if recherche :
        resultats = Articles.objects.filter( Q(type__startswith= recherche) | Q(marque__startswith= recherche) | Q(model__startswith= recherche) | Q(type__icontains= recherche) | Q(marque__icontains= recherche) | Q(model__icontains= recherche)) #model__icontains=recherche

    context = {
        "recherche":recherche,
        "resultats":resultats,
        "nbrArt":nbrArt,
    }

    return render(request, 'articles/recherche.html',context )





    

def validerPanier(request):
    if request.user.is_authenticated :
        panierUser = Panier.objects.get(user = request.user)
        totalPanier = 0
        articlesPanier = ArticlesPanier.objects.filter(panier=panierUser)

        for i in articlesPanier.all():
            article = i.article

            # Vérifier la disponibilité en stock
            if i.quantite > article.stock:
                messages.info(request,f"La quantité demandée pour l'article {article.model} dépasse le stock disponible.")
                continue  

            #totalArticle = i.quantite * i.article.prix
            # Calculer le prix total de l'article
            totalPanier += i.quantite * i.article.prix


        achat = AchatPanier.objects.create(
            utilisateur = request.user,
            total = totalPanier ,
            articles = [( f"Article No: {i.article.id}" ,f"Nom: {i.article.model}"  ,f"quantité: {i.quantite}" ) for i in articlesPanier.all() ],
            statue = "En attente de paiement"
        )   

        # Réinitialiser le panier après validation
        Panier.objects.filter(user=request.user).delete()

        return JsonResponse({ 'success':True ,  'totalPanier': totalPanier , 'achat_id':achat.id })

    else:

        messages.info(request,"Vous devez être connecter pour valider votre panier !")  
        return redirect('connection')  

def commande(request,id):
    articlesPanier = ArticlesPanier.objects.all()
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1

    if request.user.is_authenticated :
        articlesPanier = ArticlesPanier.objects.all()
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1
    #panierUser = Panier.objects.get(user = request.user)
    articlesAchat= AchatPanier.objects.get(id = id)
    
    total = articlesAchat.total
    statue = articlesAchat.statue
    context ={
        'articles':articlesAchat,
        'total':total ,
        'statue':statue,
        'nbrArt':nbrArt,

    }

    return render(request,"articles/commande.html",context)

def histCommande(request):
    articlesPanier = ArticlesPanier.objects.all()
    nbrArt = 0
    for article in articlesPanier:
        nbrArt += 1

    commandes = AchatPanier.objects.filter(utilisateur=request.user).order_by('date')
    return render(request, 'articles/histCommande.html', {'commandes': commandes ,'nbrArt': nbrArt})


def gestion(request):

    if request.user.is_authenticated :
        articles = Articles.objects.all()

        context = {
            "articles": articles,
            
        }

        return render(request,"articles/gestion.html" ,context)
    
    else:
        return redirect('connexion')

def gestionE(request):
    articles = Articles.objects.filter(categorie__name='Electroniques')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def gestionM(request):
    articles = Articles.objects.filter(categorie__name='Modes')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def gestionTelephone(request):
    articles = Articles.objects.filter(type ='Telephone')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def gestionOrdi(request):
    articles = Articles.objects.filter(type ='Ordinateurs')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def gestionAirpods(request):
    articles = Articles.objects.filter(type ='Airpods')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def gestionCasque(request):
    articles = Articles.objects.filter(type ='Casques')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def gestionMontre(request):
    articles = Articles.objects.filter(type ='Montres')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def gestionShoes(request):
    articles = Articles.objects.filter(type ='Shoes')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def gestionHabits(request):
    articles = Articles.objects.filter(type ='Habits')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def gestionAccessoires(request):
    articles = Articles.objects.filter(type ='Accessoires')

    context = {
        "articles": articles,
    }

    return render(request,"articles/gestion.html" ,context)

def ajouter(request):

    if request.method == "POST":
        forms = ArticlesForms(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            print("le formulaire est valide")

        else:
            print("le formulaire n'est pas valide")
            print(forms.errors)

        return redirect('gestion')

    else:

        forms = ArticlesForms()

    context = {
        "form":forms
    }
    return render(request, "articles/ajouter.html", context)

def modifierArt(request, idArt):
    article= Articles.objects.get(id= idArt)

    if request.method == "POST":
        forms = ArticlesForms(request.POST, request.FILES, instance=article)

        if forms.is_valid():
            forms.save()
            print("le formulaire est valide")

        else:
            print("le formulaire n'est pas valide")
            print(forms.errors)

        return redirect('gestion')

    else:

        forms = ArticlesForms(instance=article)

    context = {
        "form":forms
    }
    return render(request, "articles/modifier.html", context)

def supArticle(request, idArt):
    article= Articles.objects.get(id= idArt)

    article.delete()

    return redirect('gestion')

def rechercheG(request):
    recherche = request.GET.get('r')
    resultats = []

    if recherche :
        resultats = Articles.objects.filter( Q(type__startswith= recherche) | Q(marque__startswith= recherche) | Q(model__startswith= recherche) | Q(type__icontains= recherche) | Q(marque__icontains= recherche) | Q(model__icontains= recherche)) #model__icontains=recherche

    context = {
        "recherche":recherche,
        "articles":resultats,
    }

    return render(request, 'articles/rechercheG.html',context )

