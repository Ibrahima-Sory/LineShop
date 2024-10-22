from django.contrib import admin
from . import  models

# Register your models here.


class PanierAdmin(admin.ModelAdmin):
    list_display = ('user', 'affichage_articles', 'prix_total')

    def prix_total(self, obj):
        return f"{obj.prix_total:,.0f} FGN".replace(",", " ")
    prix_total.short_description = 'prix total' 

    def affichage_articles(self, obj):
        return obj.affichage_articles()
    affichage_articles.short_description = 'Articles dans le panier:'


admin.site.register(models.Articles)
admin.site.register(models.Categories)
admin.site.register(models.ArticlesPanier)
admin.site.register(models.Panier ,PanierAdmin)
admin.site.register(models.AchatPanier)
admin.site.register(models.Annonces)


