# Generated by Django 5.1.1 on 2024-09-09 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articlespanier_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageAn', models.ImageField(default='', upload_to='articles/')),
                ('reduction', models.IntegerField(blank=True, default=0, null=True)),
                ('prixRed', models.IntegerField(blank=True, default=0, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
            ],
        ),
    ]
