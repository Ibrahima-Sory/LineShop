# Generated by Django 5.1.1 on 2024-09-11 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_alter_articlespanier_panier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlespanier',
            name='panier',
        ),
        migrations.RemoveField(
            model_name='panier',
            name='articles',
        ),
    ]
