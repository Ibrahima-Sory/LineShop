"""
URL configuration for LineShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include ,path
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from accounts.views import CustomPasswordResetView 




urlpatterns = [
    path('', include('articles.urls')),
    path('accounts', include('accounts.urls')),
    #path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
   # Vue pour entrer l’email pour la réinitialisation du mot de passe
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',  # Page de saisie de l'email
            html_email_template_name='registration/password_reset_email.html',  # Template HTML
        ),
        name='password_reset'
    ),

    # Vue pour informer que l’email de réinitialisation a été envoyé
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # Vue pour entrer le nouveau mot de passe à l’aide du lien envoyé par email
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    # Vue pour confirmer que le mot de passe a été réinitialisé avec succès
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

    #path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),   

    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
