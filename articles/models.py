from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Categories(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name 
        


class Articles(models.Model):
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    type = models.CharField( max_length=50 ,blank=True, null=True)
    marque = models.CharField( max_length=50 ,blank=True, null=True)
    model = models.CharField(max_length=50 ,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='articles/', default= "" )
    prix = models.IntegerField(default= 0 ,blank=True, null=True)
    specificité = models.CharField( max_length=50 ,blank=True, null=True)
    enpromo = models.BooleanField(default=False)
    prix_promo = models.IntegerField(default= 0 ,blank=True, null=True)
    stock = models.IntegerField(default=1 ,blank=True, null=True)
    #quantite = models.PositiveIntegerField(default=0)

    def prix_formater(self):
        return f"{self.prix:,.0f}".replace(",", " ")
    
    def prixPromo_formater(self):
        return f"{self.prix_promo:,.0f}".replace(",", " ")

    def __str__(self):
    
        return self.model 
    
class Annonces(models.Model):
    #articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50 ,blank=True, null=True)
    imageAn = models.ImageField(upload_to='articles/', default= "" )
    reduction = models.IntegerField(default= 0 ,blank=True, null=True)
    prixRed = models.IntegerField(default= 0 ,blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.titre 


class Panier(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    articles = models.ManyToManyField(Articles , through='ArticlesPanier')
    #nbrArticles = models.IntegerField(blank=True, null=True)

    @property
    def prix_total(self):
        total = 0
        for article_panier in self.articlespanier_set.all():
            if article_panier.article.enpromo:
                total += article_panier.article.prix_promo * article_panier.quantite
            else:
                total += article_panier.article.prix * article_panier.quantite
        return total
    
    
    def affichage_articles(self):
        articles = ", ".join([f"{i.article.model} (x {i.quantite})" for i in self.articlespanier_set.all() ])
        return articles if articles else "Aucun article dans le panier"

    def __str__(self):
        return f"Panier de {self.user.email}"

class ArticlesPanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE ,default=0, blank=True, null=True)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.article.model
    
class AchatArticle(models.Model):
    
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    total = models.PositiveIntegerField(default=0 ,blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=50 ,blank=True, null=True)
    adresse = models.CharField(max_length=50 ,blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = [
    ('En attente', 'En attente'),
    ('Confirmé', 'Confirmé'),
    ('Livré', 'Livré'),
    ]
    statue = models.CharField(max_length=50, choices=STATUS_CHOICES,default="En attente")
    
    def __str__(self):
        return f"{self.article.model} (x{self.quantite})" 

    def prix_total(self):
        return self.quantite * self.article.prix    



