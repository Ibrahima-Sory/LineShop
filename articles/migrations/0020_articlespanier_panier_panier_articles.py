# Generated by Django 5.1.1 on 2024-09-11 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_remove_articlespanier_panier_remove_panier_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlespanier',
            name='panier',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.panier'),
        ),
        migrations.AddField(
            model_name='panier',
            name='articles',
            field=models.ManyToManyField(through='articles.ArticlesPanier', to='articles.articles'),
        ),
    ]
