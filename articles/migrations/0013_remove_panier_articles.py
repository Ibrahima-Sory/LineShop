# Generated by Django 5.1.1 on 2024-09-11 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_articlespanier_user_panier_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='articles',
        ),
    ]
