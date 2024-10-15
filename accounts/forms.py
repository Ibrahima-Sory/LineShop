from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserShop 

class EnregistrementForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    adresse = forms.CharField()
    
    
    class Meta:
        model = UserShop
        fields = ['last_name','first_name', 'email', 'phone','adresse' ,'password1', 'password2']
        labels = {'Nom':'last_name', 'Prenom': 'first_name', 'Email':'email' ,'Telephone': 'phone', 'Adresse': 'adresse', 'Mots de passe':'password1' , 'Confirmation':'password2'}   

    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data['email'] 
        
        if commit:
            user.save()
        return user 
    

class ConnexionForm(AuthenticationForm):
    username = forms.EmailField(label="Email" , widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email:'}))
    password = forms.CharField(label="Mot de passe" ,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))


