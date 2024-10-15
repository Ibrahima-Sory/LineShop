from django import forms  
from .models import Articles , Categories

class ArticlesForms(forms.ModelForm):
    categorie = forms.ModelChoiceField(queryset= Categories.objects.all(), label="Categorie")

    class Meta:
        model = Articles
        fields = ['categorie','model', 'type','image' , 'description', 'marque', 'prix', 'specificité', 'enpromo', 'prix_promo', 'stock']
        labels = { 'Model':'model', 'Type':'type' , 'Image':'image', 'Description':'description','Marque':'marque', 'Prix':'prix', 'Specificité':'specificité','En promo ?':'enpromo', 'Prix promo':'prix_promo', 'Stock':'stock' }