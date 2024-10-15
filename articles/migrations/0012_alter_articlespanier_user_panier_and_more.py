# Generated by Django 5.1.1 on 2024-09-11 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_articles_prix_promo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlespanier',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articlesPanier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.ManyToManyField(related_name='panier', through='articles.ArticlesPanier', to='articles.articles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='articlespanier',
            name='panier',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles_du_panier', to='articles.panier'),
        ),
    ]
